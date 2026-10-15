"""FFmpeg and FFprobe utility checks and media inspection."""

import json
import logging
import os
import shutil
import subprocess
from pathlib import Path
from typing import Any, Dict

for _ff_dir in (r"D:\tools\ffmpeg\bin", r"C:\ffmpeg\bin"):
    if os.path.isdir(_ff_dir) and _ff_dir not in os.environ.get("PATH", ""):
        os.environ["PATH"] = _ff_dir + os.pathsep + os.environ.get("PATH", "")

logger = logging.getLogger(__name__)


def check_ffmpeg_installed() -> bool:
    """Check if ffmpeg executable exists in PATH."""
    return shutil.which("ffmpeg") is not None


def check_ffprobe_installed() -> bool:
    """Check if ffprobe or ffmpeg executable exists in PATH."""
    return shutil.which("ffprobe") is not None or shutil.which("ffmpeg") is not None


def get_ffmpeg_version() -> str:
    """Return version string of installed ffmpeg."""
    try:
        res = subprocess.run(
            ["ffmpeg", "-version"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )
        return res.stdout.splitlines()[0] if res.stdout else "Unknown"
    except Exception as e:
        logger.error(f"Error checking ffmpeg version: {e}")
        return "Not available"


def probe_media(file_path: Path) -> Dict[str, Any]:
    """Inspect media file using ffprobe (or ffmpeg -i fallback) and return metadata."""
    if shutil.which("ffprobe") is not None:
        cmd = [
            "ffprobe",
            "-v", "quiet",
            "-print_format", "json",
            "-show_format",
            "-show_streams",
            str(file_path),
        ]
        try:
            res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
            data = json.loads(res.stdout)
            streams = data.get("streams", [])
            format_info = data.get("format", {})

            has_video = False
            has_audio = False
            width = 0
            height = 0
            video_codec = ""
            audio_codec = ""
            duration = 0.0

            for s in streams:
                codec_type = s.get("codec_type")
                if codec_type == "video" and not has_video:
                    has_video = True
                    width = int(s.get("width", 0))
                    height = int(s.get("height", 0))
                    video_codec = s.get("codec_name", "")
                    if "duration" in s:
                        try:
                            duration = max(duration, float(s["duration"]))
                        except (ValueError, TypeError):
                            pass
                elif codec_type == "audio" and not has_audio:
                    has_audio = True
                    audio_codec = s.get("codec_name", "")
                    if "duration" in s:
                        try:
                            duration = max(duration, float(s["duration"]))
                        except (ValueError, TypeError):
                            pass

            if duration == 0.0 and "duration" in format_info:
                try:
                    duration = float(format_info["duration"])
                except (ValueError, TypeError):
                    pass

            return {
                "has_video": has_video,
                "has_audio": has_audio,
                "width": width,
                "height": height,
                "video_codec": video_codec,
                "audio_codec": audio_codec,
                "duration": duration,
                "format_name": format_info.get("format_name", ""),
                "size_bytes": int(format_info.get("size", 0)),
            }
        except Exception as e:
            logger.warning(f"ffprobe failed for {file_path}, falling back to ffmpeg -i: {e}")

    if not check_ffmpeg_installed():
        raise RuntimeError("Neither ffprobe nor ffmpeg is installed or in PATH")

    import re
    res = subprocess.run(
        ["ffmpeg", "-i", str(file_path)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    info = res.stderr or ""
    has_video = "Video:" in info
    has_audio = "Audio:" in info
    width, height = 0, 0
    m_res = re.search(r"Video:.*?,\s*(\d{2,5})x(\d{2,5})", info)
    if m_res:
        width, height = int(m_res.group(1)), int(m_res.group(2))
    duration = 0.0
    m_dur = re.search(r"Duration:\s*(\d+):(\d+):(\d+(?:\.\d+)?)", info)
    if m_dur:
        duration = int(m_dur.group(1)) * 3600 + int(m_dur.group(2)) * 60 + float(m_dur.group(3))
    m_vc = re.search(r"Video:\s*([a-zA-Z0-9_]+)", info)
    m_ac = re.search(r"Audio:\s*([a-zA-Z0-9_]+)", info)
    return {
        "has_video": has_video,
        "has_audio": has_audio,
        "width": width,
        "height": height,
        "video_codec": m_vc.group(1) if m_vc else "",
        "audio_codec": m_ac.group(1) if m_ac else "",
        "duration": duration,
        "format_name": file_path.suffix.lstrip("."),
        "size_bytes": file_path.stat().st_size if file_path.exists() else 0,
    }
