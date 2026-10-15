"""Autonomous Competitor Monitor for @aryafeed.in.

Monitors 4 target competitor accounts:
1. @rvcjinsta (RVCJ Media - viral news, meme cards, trending stories)
2. @flirting.lines (pickup lines, dating banter, relatable thoughts)
3. @comedyculture.in (relatable Indian memes, humor)
4. @adultsociety (late night thoughts, youth culture, viral clips)

Autonomous Rules:
- If image/video is CLEAN (no competitor handle/branding on the visual):
  -> Directly stamps [ ARYAFEED ] watermark on bottom-right and posts to @aryafeed.in.
  -> Same audio preserved if video has audio; no music added if video had none.
- If image/video has COMPETITOR TITLE/BRANDING:
  -> Sends alert to Telegram bot.
  -> Cleans the title, replaces branding with [ ARYAFEED ] signature pill.
  -> Keeps exact same audio.
  -> Posts to Instagram and notifies Telegram with preview.
"""

import asyncio
import hashlib
import json
import logging
import os
import re
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import aiosqlite
import requests
from PIL import Image

from bot.services.instagram_service import instagram_service
from bot.services.video_engine import stamp_image_watermark, stamp_video_watermark
from bot.utils.config import config
from database.db import db_manager

logger = logging.getLogger(__name__)

COMPETITOR_ACCOUNTS = [
    "rvcjinsta",
    "flirting.lines",
    "comedyculture.in",
    "adultsociety",
]

COMPETITOR_HANDLES = [
    "rvcj",
    "rvcjinsta",
    "comedyculture",
    "comedyculture.in",
    "adultsociety",
    "flirting.lines",
    "flirtinglines",
]

DEFAULT_ADMIN_CHAT_ID = 5381201341


class CompetitorMonitorService:
    """Service to monitor competitor Instagram accounts and process/rebrand content."""

    def __init__(self):
        self.db_path = config.database_path

    async def init_tables(self) -> None:
        """Create competitor_monitored_posts table if not exists."""
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute("""
                CREATE TABLE IF NOT EXISTS competitor_monitored_posts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    account_username TEXT NOT NULL,
                    post_id TEXT NOT NULL,
                    media_type TEXT,
                    caption TEXT,
                    has_competitor_branding INTEGER DEFAULT 0,
                    downloaded_file TEXT,
                    processed_file TEXT,
                    instagram_url TEXT,
                    posted_to_ig INTEGER DEFAULT 0,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    UNIQUE(account_username, post_id)
                );
            """)
            await db.execute("""
                CREATE INDEX IF NOT EXISTS idx_competitor_posts 
                ON competitor_monitored_posts(account_username, post_id);
            """)
            await db.commit()

    async def is_post_processed(self, username: str, post_id: str) -> bool:
        """Check if post was already fetched and processed."""
        async with aiosqlite.connect(self.db_path) as db:
            async with db.execute(
                "SELECT 1 FROM competitor_monitored_posts WHERE account_username = ? AND post_id = ?",
                (username, str(post_id)),
            ) as cursor:
                return bool(await cursor.fetchone())

    async def record_processed_post(
        self,
        username: str,
        post_id: str,
        media_type: str,
        caption: str,
        has_branding: bool,
        downloaded_file: str,
        processed_file: str,
        posted_to_ig: bool,
        instagram_url: Optional[str] = None,
    ) -> None:
        """Record post in SQLite database."""
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute("""
                INSERT OR REPLACE INTO competitor_monitored_posts (
                    account_username, post_id, media_type, caption,
                    has_competitor_branding, downloaded_file, processed_file,
                    posted_to_ig, instagram_url
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
            """, (
                username,
                str(post_id),
                media_type,
                caption,
                1 if has_branding else 0,
                downloaded_file,
                processed_file,
                1 if posted_to_ig else 0,
                instagram_url,
            ))
            await db.commit()

    def check_competitor_branding(self, text_or_caption: str) -> bool:
        """Check if text contains any competitor account handles or branding."""
        clean = (text_or_caption or "").lower()
        return any(handle in clean for handle in COMPETITOR_HANDLES)

    def clean_caption_for_aryafeed(self, raw_caption: str, source_account: str) -> str:
        """Strip competitor handles/promos, replace competitor titles with AryaFeed, and format clean caption."""
        lines = (raw_caption or "").split("\n")
        clean_lines = []
        for line in lines:
            line_lower = line.lower()
            # Skip lines with competitor promo or handles
            if any(h in line_lower for h in COMPETITOR_HANDLES):
                continue
            if any(p in line_lower for p in ["follow @", "follow us", "dm for", "link in bio"]):
                continue
            clean_lines.append(line)

        body = "\n".join(clean_lines).strip()
        # Replace any residual competitor titles with AryaFeed
        for comp_name in ["rvcjinsta", "rvcj", "comedyculture.in", "comedyculture", "flirting.lines", "flirtinglines", "adultsociety"]:
            body = re.sub(re.escape(comp_name), "AryaFeed", body, flags=re.IGNORECASE)

        if not body:
            body = "⚡ Daily dose of viral stories, memes & thoughts!"

        hashtags = "\n\nFollow @aryafeed.in for daily buzz ⚡\n#aryafeed #viral #trending #reels #memes #explore #india"
        return body + hashtags

    def clean_and_rebrand_image(
        self,
        input_path: Path,
        output_path: Path,
        target_username: str,
        brand: str = "ARYAFEED",
    ) -> Path:
        """Detect competitor logos, inpaint them seamlessly, and apply [ ARYAFEED ] branding."""
        import cv2
        import numpy as np
        from PIL import Image, ImageDraw
        from bot.services.text_overlay import load_font

        cv_img = cv2.imread(str(input_path))
        if cv_img is None:
            return stamp_image_watermark(input_path, output_path, brand)

        h, w = cv_img.shape[:2]
        scale = max(0.5, min(2.5, w / 1080.0))
        clean_u = (target_username or "").lower().replace(".", "")

        if "comedyculture" in clean_u:
            # 1. Inpaint top-left logo (circular red logo + ComedyCulture text)
            mask = np.zeros((h, w), dtype=np.uint8)
            mask[0:int(h * 0.10), 0:int(w * 0.26)] = 255
            inp = cv2.inpaint(cv_img, mask, 5, cv2.INPAINT_TELEA)

            pil_img = Image.fromarray(cv2.cvtColor(inp, cv2.COLOR_BGR2RGB))
            draw = ImageDraw.Draw(pil_img)

            # Draw signature >> aryafeed.in at top-left
            font_size = int(24 * scale)
            try:
                sig_font = ImageFont.truetype("C:/Windows/Fonts/ariblk.ttf", font_size)
            except Exception:
                sig_font = load_font(config.font_path, font_size)

            white = (255, 255, 255)
            red = (235, 35, 45)
            shadow = (15, 25, 35)
            sx = int(24 * scale)
            sy = int(24 * scale)

            w_ch = draw.textbbox((0, 0), ">> ", font=sig_font)[2]
            w_af = draw.textbbox((0, 0), "aryafeed", font=sig_font)[2]

            for dx, dy in [(1, 1), (2, 2)]:
                draw.text((sx + dx, sy + dy), ">> ", font=sig_font, fill=shadow)
                draw.text((sx + w_ch + dx, sy + dy), "aryafeed", font=sig_font, fill=shadow)
                draw.text((sx + w_ch + w_af + dx, sy + dy), ".in", font=sig_font, fill=shadow)

            draw.text((sx, sy), ">> ", font=sig_font, fill=red)
            draw.text((sx + w_ch, sy), "aryafeed", font=sig_font, fill=white)
            draw.text((sx + w_ch + w_af, sy), ".in", font=sig_font, fill=red)

        elif "flirtinglines" in clean_u:
            # Inpaint top-left logo (flirting lines >>)
            mask = np.zeros((h, w), dtype=np.uint8)
            mask[0:int(h * 0.12), 0:int(w * 0.25)] = 255
            inp = cv2.inpaint(cv_img, mask, 4, cv2.INPAINT_TELEA)

            pil_img = Image.fromarray(cv2.cvtColor(inp, cv2.COLOR_BGR2RGB))
            draw = ImageDraw.Draw(pil_img)

            # Locked Signature Style: >> aryafeed.in (Red >>, White aryafeed, Red .in)
            font_size = int(22 * scale)
            try:
                sig_font = ImageFont.truetype("C:/Windows/Fonts/ariblk.ttf", font_size)
            except Exception:
                sig_font = load_font(config.font_path, font_size)

            white = (255, 255, 255)
            red = (235, 35, 45)
            shadow = (15, 25, 35)
            sx = int(28 * scale)
            sy = int(22 * scale)

            w_ch = draw.textbbox((0, 0), ">> ", font=sig_font)[2]
            w_af = draw.textbbox((0, 0), "aryafeed", font=sig_font)[2]

            for dx, dy in [(1, 1), (2, 2)]:
                draw.text((sx + dx, sy + dy), ">> ", font=sig_font, fill=shadow)
                draw.text((sx + w_ch + dx, sy + dy), "aryafeed", font=sig_font, fill=shadow)
                draw.text((sx + w_ch + w_af + dx, sy + dy), ".in", font=sig_font, fill=shadow)

            draw.text((sx, sy), ">> ", font=sig_font, fill=red)
            draw.text((sx + w_ch, sy), "aryafeed", font=sig_font, fill=white)
            draw.text((sx + w_ch + w_af, sy), ".in", font=sig_font, fill=red)

        elif "rvcj" in clean_u:
            # Check if RVCJ top yellow logo exists at top-center
            roi_top = cv_img[:int(h * 0.12), int(w * 0.35):int(w * 0.65)]
            hsv_top = cv2.cvtColor(roi_top, cv2.COLOR_BGR2HSV)
            mask_yellow = cv2.inRange(hsv_top, np.array([20, 100, 100]), np.array([35, 255, 255]))
            has_top_box = (np.count_nonzero(mask_yellow) > 500)

            # Check if mid watermark exists
            roi_mid = cv_img[int(h * 0.44):int(h * 0.52), int(w * 0.70):int(w * 0.85)]
            hsv_mid = cv2.cvtColor(roi_mid, cv2.COLOR_BGR2HSV)
            mask_cyan = cv2.inRange(hsv_mid, np.array([80, 80, 80]), np.array([105, 255, 255]))
            has_mid_wm = (np.count_nonzero(mask_cyan) > 50)

            if has_mid_wm:
                mask_mid = np.zeros((h, w), dtype=np.uint8)
                mask_mid[int(h * 0.44):int(h * 0.52), int(w * 0.70):int(w * 0.85)] = 255
                cv_img = cv2.inpaint(cv_img, mask_mid, 4, cv2.INPAINT_TELEA)

            pil_img = Image.fromarray(cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB))
            draw = ImageDraw.Draw(pil_img)

            # Draw locked signature >> aryafeed.in branding
            font_size = int(24 * scale)
            try:
                sig_font = ImageFont.truetype("C:/Windows/Fonts/ariblk.ttf", font_size)
            except Exception:
                sig_font = load_font(config.font_path, font_size)

            white = (255, 255, 255)
            red = (235, 35, 45)
            shadow = (15, 25, 35)

            w_ch = draw.textbbox((0, 0), ">> ", font=sig_font)[2]
            w_af = draw.textbbox((0, 0), "aryafeed", font=sig_font)[2]
            w_in = draw.textbbox((0, 0), ".in", font=sig_font)[2]
            tot_w = w_ch + w_af + w_in

            if has_top_box:
                box_x1 = int(w * 0.38)
                box_x2 = int(w * 0.62)
                top_bar_h = int(46 * scale)
                sample_color = pil_img.getpixel((int(w * 0.2), int(20 * scale)))
                draw.rectangle([(box_x1, 0), (box_x2, top_bar_h)], fill=sample_color)
                draw.rectangle([(box_x1, top_bar_h + 1), (box_x2, int(120 * scale))], fill=(255, 255, 255))
                sx = (w - tot_w) // 2
                sy = int(28 * scale)
            else:
                sx = int(24 * scale)
                sy = int(24 * scale)

            for dx, dy in [(1, 1), (2, 2)]:
                draw.text((sx + dx, sy + dy), ">> ", font=sig_font, fill=shadow)
                draw.text((sx + w_ch + dx, sy + dy), "aryafeed", font=sig_font, fill=shadow)
                draw.text((sx + w_ch + w_af + dx, sy + dy), ".in", font=sig_font, fill=shadow)

            draw.text((sx, sy), ">> ", font=sig_font, fill=red)
            draw.text((sx + w_ch, sy), "aryafeed", font=sig_font, fill=white)
            draw.text((sx + w_ch + w_af, sy), ".in", font=sig_font, fill=red)

            footer_y = int(h * 0.95)
            draw.rectangle([(0, footer_y), (w, h)], fill=(12, 12, 16))
            footer_font = load_font(config.font_path, int(26 * scale))
            ftext = "FOLLOW @ARYAFEED.IN FOR VIRAL UPDATES"
            fbbox = draw.textbbox((0, 0), ftext, font=footer_font)
            ftw = fbbox[2] - fbbox[0]
            fth = fbbox[3] - fbbox[1]
            ftx = (w - ftw) // 2
            fty = footer_y + (h - footer_y - fth) // 2 - fbbox[1]
            draw.text((ftx, fty), ftext, font=footer_font, fill=(255, 220, 0, 255))

        else:
            mask = np.zeros((h, w), dtype=np.uint8)
            mask[0:int(h * 0.08), 0:int(w * 0.20)] = 255
            inp = cv2.inpaint(cv_img, mask, 4, cv2.INPAINT_TELEA)

            pil_img = Image.fromarray(cv2.cvtColor(inp, cv2.COLOR_BGR2RGB))
            draw = ImageDraw.Draw(pil_img)

            font_size = int(22 * scale)
            try:
                sig_font = ImageFont.truetype("C:/Windows/Fonts/ariblk.ttf", font_size)
            except Exception:
                sig_font = load_font(config.font_path, font_size)

            white = (255, 255, 255)
            red = (235, 35, 45)
            shadow = (15, 25, 35)
            sx = int(20 * scale)
            sy = int(20 * scale)

            w_ch = draw.textbbox((0, 0), ">> ", font=sig_font)[2]
            w_af = draw.textbbox((0, 0), "aryafeed", font=sig_font)[2]

            for dx, dy in [(1, 1), (2, 2)]:
                draw.text((sx + dx, sy + dy), ">> ", font=sig_font, fill=shadow)
                draw.text((sx + w_ch + dx, sy + dy), "aryafeed", font=sig_font, fill=shadow)
                draw.text((sx + w_ch + w_af + dx, sy + dy), ".in", font=sig_font, fill=shadow)

            draw.text((sx, sy), ">> ", font=sig_font, fill=red)
            draw.text((sx + w_ch, sy), "aryafeed", font=sig_font, fill=white)
            draw.text((sx + w_ch + w_af, sy), ".in", font=sig_font, fill=red)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        pil_img.save(output_path, "JPEG", quality=95)
        return output_path

    async def scan_and_rebrand_competitors(
        self,
        chat_id: int = DEFAULT_ADMIN_CHAT_ID,
        bot = None,
    ) -> List[Dict[str, Any]]:
        """Main autonomous loop: scans the 4 competitor accounts, downloads fresh posts,
        cleans branding or posts direct, and uploads to @aryafeed.in."""
        await self.init_tables()
        results = []

        # 1. Check if authenticated client is available
        cl = await instagram_service.get_authenticated_client(chat_id)
        if not cl:
            logger.info("[CompetitorMonitor] Instagram client not logged in. Waiting for /insta_login.")
            return results

        for target_username in COMPETITOR_ACCOUNTS:
            try:
                logger.info(f"[CompetitorMonitor] Checking @{target_username}...")
                target_user_id = await asyncio.to_thread(cl.user_id_from_username, target_username)
                if not target_user_id:
                    continue

                medias = await asyncio.to_thread(cl.user_medias, target_user_id, 3)
                for m in (medias or []):
                    post_id = str(getattr(m, "pk", getattr(m, "id", None)))
                    if not post_id or await self.is_post_processed(target_username, post_id):
                        continue

                    logger.info(f"[CompetitorMonitor] Found fresh post {post_id} from @{target_username}")
                    media_type = "video" if getattr(m, "media_type", 1) == 2 else "image"
                    raw_caption = getattr(m, "caption_text", "") or ""
                    clean_caption = self.clean_caption_for_aryafeed(raw_caption, target_username)

                    # Download media file
                    timestamp = int(datetime.now(timezone.utc).timestamp())
                    ext = ".mp4" if media_type == "video" else ".jpg"
                    dl_path = config.input_dir / f"comp_{target_username}_{post_id}_{timestamp}{ext}"

                    if media_type == "video":
                        video_url = getattr(m, "video_url", None)
                        if not video_url:
                            continue
                        r = requests.get(video_url, stream=True, timeout=20)
                        with open(dl_path, "wb") as f:
                            for chunk in r.iter_content(chunk_size=65536):
                                f.write(chunk)
                    else:
                        img_url = getattr(m, "thumbnail_url", None)
                        if not img_url:
                            # Try candidate resources
                            resources = getattr(m, "resources", None)
                            if resources and len(resources) > 0:
                                img_url = getattr(resources[0], "thumbnail_url", None)
                        if not img_url:
                            continue
                        r = requests.get(img_url, stream=True, timeout=15)
                        with open(dl_path, "wb") as f:
                            for chunk in r.iter_content(chunk_size=32768):
                                f.write(chunk)

                    if not dl_path.exists() or dl_path.stat().st_size < 1000:
                        continue

                    # Check for competitor branding
                    has_branding = self.check_competitor_branding(raw_caption)

                    # Process file: clean competitor branding and rebrand with [ ARYAFEED ]
                    processed_path = config.output_dir / f"arya_{target_username}_{post_id}_{timestamp}{ext}"

                    if media_type == "video":
                        # Embed watermark preserving original audio
                        await asyncio.to_thread(stamp_video_watermark, dl_path, processed_path, "ARYAFEED")
                    else:
                        # Clean competitor logo/strip and stamp [ ARYAFEED ] branding
                        await asyncio.to_thread(self.clean_and_rebrand_image, dl_path, processed_path, target_username, "ARYAFEED")

                    # Upload to Instagram
                    ig_result = {}
                    if media_type == "video":
                        ig_result = await instagram_service.upload_reel(
                            chat_id=chat_id,
                            video_path=processed_path,
                            caption=clean_caption,
                        )
                    else:
                        ig_result = await instagram_service.upload_photo(
                            chat_id=chat_id,
                            photo_path=processed_path,
                            caption=clean_caption,
                        )

                    posted_to_ig = ig_result.get("success", False)
                    ig_url = ig_result.get("url")

                    await self.record_processed_post(
                        username=target_username,
                        post_id=post_id,
                        media_type=media_type,
                        caption=clean_caption,
                        has_branding=has_branding,
                        downloaded_file=str(dl_path),
                        processed_file=str(processed_path),
                        posted_to_ig=posted_to_ig,
                        instagram_url=ig_url,
                    )

                    # Telegram notification
                    if bot:
                        try:
                            status_badge = "✅ *Clean Media — Auto-Posted Live!*" if not has_branding else "⚡ *Branded Media — Cleaned & Published!*"
                            caption_text = (
                                f"{status_badge}\n\n"
                                f"👤 *Source:* `@{target_username}`\n"
                                f"📂 *Type:* {'Reel' if media_type == 'video' else 'Meme Card / Photo'}\n"
                                f"🏷️ *Brand:* `[ ARYAFEED ]` (Bottom Right)\n"
                                f"🎵 *Audio:* Preserved Original\n\n"
                            )
                            if ig_url:
                                caption_text += f"🚀 [Watch Live on Instagram]({ig_url})\n"
                            elif ig_result.get("error"):
                                caption_text += f"⚠️ *Instagram Note:* {ig_result.get('error')}\n"

                            if media_type == "video":
                                with open(processed_path, "rb") as vf:
                                    await bot.send_video(
                                        chat_id=chat_id,
                                        video=vf,
                                        caption=caption_text,
                                        parse_mode="Markdown",
                                    )
                            else:
                                with open(processed_path, "rb") as pf:
                                    await bot.send_photo(
                                        chat_id=chat_id,
                                        photo=pf,
                                        caption=caption_text,
                                        parse_mode="Markdown",
                                    )
                        except Exception as e:
                            logger.warning(f"[CompetitorMonitor] Telegram alert failed: {e}")

                    results.append({
                        "account": target_username,
                        "post_id": post_id,
                        "media_type": media_type,
                        "posted": posted_to_ig,
                        "url": ig_url,
                    })

                    # Small delay between account posts to avoid rapid burst
                    await asyncio.sleep(5)

            except Exception as e:
                logger.warning(f"[CompetitorMonitor] Error scanning @{target_username}: {e}")

        return results

    async def process_media_item(
        self,
        target_username: str,
        media_obj: Any,
        chat_id: int,
        bot = None,
    ) -> Optional[Dict[str, Any]]:
        """Process a single newly detected post immediately:
        - If clean: stamp [ ARYAFEED ] watermark, preserve original audio, post to @aryafeed.in.
        - If branded: clean caption and branding, stamp [ ARYAFEED ] pill, preserve original audio, post to @aryafeed.in.
        """
        post_id = str(getattr(media_obj, "pk", getattr(media_obj, "id", None)))
        if not post_id or await self.is_post_processed(target_username, post_id):
            return None

        logger.info(f"[SpySentinel] 🎯 NEW POST DETECTED on @{target_username}! Post ID: {post_id}")
        media_type = "video" if getattr(media_obj, "media_type", 1) == 2 else "image"
        raw_caption = getattr(media_obj, "caption_text", "") or ""
        clean_caption = self.clean_caption_for_aryafeed(raw_caption, target_username)

        timestamp = int(datetime.now(timezone.utc).timestamp())
        ext = ".mp4" if media_type == "video" else ".jpg"
        dl_path = config.input_dir / f"spy_{target_username}_{post_id}_{timestamp}{ext}"

        if media_type == "video":
            video_url = getattr(media_obj, "video_url", None)
            if not video_url:
                return None
            r = requests.get(video_url, stream=True, timeout=25)
            with open(dl_path, "wb") as f:
                for chunk in r.iter_content(chunk_size=65536):
                    f.write(chunk)
        else:
            img_url = getattr(media_obj, "thumbnail_url", None)
            if not img_url:
                resources = getattr(media_obj, "resources", None)
                if resources and len(resources) > 0:
                    img_url = getattr(resources[0], "thumbnail_url", None)
            if not img_url:
                return None
            r = requests.get(img_url, stream=True, timeout=20)
            with open(dl_path, "wb") as f:
                for chunk in r.iter_content(chunk_size=32768):
                    f.write(chunk)

        if not dl_path.exists() or dl_path.stat().st_size < 1000:
            return None

        has_branding = self.check_competitor_branding(raw_caption)
        processed_path = config.output_dir / f"arya_spy_{target_username}_{post_id}_{timestamp}{ext}"

        # Determine destination account & branding based on competitor niche
        is_news_competitor = (target_username.lower() in ("rvcj", "rvcjinsta"))
        dest_account = "arya" if is_news_competitor else "night"
        dest_brand = "ARYAFEED" if is_news_competitor else "NIGHT THOUGHT"
        dest_handle = "@aryafeed.in" if is_news_competitor else "@night_thought_12"

        if media_type == "video":
            # Preserve original audio stream, embed watermark
            await asyncio.to_thread(stamp_video_watermark, dl_path, processed_path, dest_brand)
        else:
            # Clean competitor logo/strip and stamp branding
            await asyncio.to_thread(self.clean_and_rebrand_image, dl_path, processed_path, target_username, dest_brand)

        # Upload strictly to the matching account
        if media_type == "video":
            ig_result = await instagram_service.upload_reel(
                chat_id=chat_id,
                video_path=processed_path,
                caption=clean_caption,
                target_account=dest_account,
            )
        else:
            ig_result = await instagram_service.upload_photo(
                chat_id=chat_id,
                photo_path=processed_path,
                caption=clean_caption,
                target_account=dest_account,
            )

        posted_to_ig = ig_result.get("success", False)
        ig_url = ig_result.get("url")

        await self.record_processed_post(
            username=target_username,
            post_id=post_id,
            media_type=media_type,
            caption=clean_caption,
            has_branding=has_branding,
            downloaded_file=str(dl_path),
            processed_file=str(processed_path),
            posted_to_ig=posted_to_ig,
            instagram_url=ig_url,
        )

        # Notify Telegram
        if bot:
            try:
                status_badge = "⚡ *SPY SENTINEL: Clean Post Auto-Uploaded!*" if not has_branding else "⚡ *SPY SENTINEL: Branded Post Cleaned & Uploaded!*"
                caption_text = (
                    f"{status_badge}\n\n"
                    f"👤 *Source:* `@{target_username}`\n"
                    f"📂 *Type:* {'Reel' if media_type == 'video' else 'Meme Card / Photo'}\n"
                    f"🏷️ *Brand:* `[ {dest_brand} ]` (Bottom Right)\n"
                    f"🎵 *Audio:* Preserved Original\n\n"
                )
                if ig_url:
                    caption_text += f"🚀 [Live on {dest_handle}]({ig_url})\n"
                elif ig_result.get("error"):
                    caption_text += f"⚠️ *Instagram Note:* {ig_result.get('error')}\n"

                if media_type == "video":
                    with open(processed_path, "rb") as vf:
                        await bot.send_video(
                            chat_id=chat_id,
                            video=vf,
                            caption=caption_text,
                            parse_mode="Markdown",
                        )
                else:
                    with open(processed_path, "rb") as pf:
                        await bot.send_photo(
                            chat_id=chat_id,
                            photo=pf,
                            caption=caption_text,
                            parse_mode="Markdown",
                        )
            except Exception as e:
                logger.warning(f"[SpySentinel] Telegram alert failed: {e}")

        return {
            "account": target_username,
            "post_id": post_id,
            "media_type": media_type,
            "posted": posted_to_ig,
            "url": ig_url,
        }

    async def run_realtime_spy_sentinel(
        self,
        chat_id: int = DEFAULT_ADMIN_CHAT_ID,
        bot = None,
    ) -> None:
        """Continuous Real-Time Sentinel Loop:
        Keeps 24/7 watch on the 4 competitor accounts.
        The moment any new post is published, immediately processes and uploads to @aryafeed.in!
        """
        await self.init_tables()
        logger.info(f"[SpySentinel] 🚨 24/7 Real-Time Spy Sentinel ACTIVATED on: {', '.join(COMPETITOR_ACCOUNTS)}")

        while True:
            try:
                cl = await instagram_service.get_authenticated_client(chat_id)
                if not cl:
                    # Client not logged in yet, wait and retry
                    await asyncio.sleep(60)
                    continue

                for target_username in COMPETITOR_ACCOUNTS:
                    try:
                        target_user_id = await asyncio.to_thread(cl.user_id_from_username, target_username)
                        if target_user_id:
                            medias = await asyncio.to_thread(cl.user_medias, target_user_id, 2)
                            for m in (medias or []):
                                await self.process_media_item(target_username, m, chat_id, bot)
                    except Exception as e:
                        err_str = str(e).lower()
                        logger.warning(f"[SpySentinel] Watch error for @{target_username}: {e}")
                        if any(k in err_str for k in ("401", "403", "unauthorized", "login_required")):
                            logger.info("[SpySentinel] Instagram session unauthenticated or expired. Pausing watch for 5 minutes.")
                            await asyncio.sleep(300)
                            break

                    # Stagger 15s between account checks for continuous, smooth monitoring
                    await asyncio.sleep(15)

            except asyncio.CancelledError:
                logger.info("[SpySentinel] Sentinel cancelled.")
                break
            except Exception as e:
                logger.exception(f"[SpySentinel] Sentinel loop error: {e}")
                await asyncio.sleep(60)


# Singleton instance
competitor_monitor_service = CompetitorMonitorService()
