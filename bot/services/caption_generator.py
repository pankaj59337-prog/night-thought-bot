"""Auto-Caption & Viral Hashtag Generation Engine for Instagram Reels (@night_thought_12)."""

import random
from typing import List, Optional

# High-CTR CTAs tailored for flirty, aesthetic & viral reels
CTAS: List[str] = [
    "Drop a '🖤' if you feel this...",
    "Save this for late night vibes 🌙✨",
    "Tag your 2 AM person 🥀",
    "Double tap if this hit home ❤️‍🩹",
    "Share with someone who needs to see this 💬",
    "Comment your mood in one emoji 🌚",
    "Rehne do cutie, sach bolna allowed nahi hai 🤫",
    "Don't forget to save this 📌",
]

# Naughty / flirty contextual teasers
TEASERS: List[str] = [
    "Some thoughts are just better left unspoken... or maybe not 🥀🖤",
    "Sharafat ka zamana gaya, late night vibes only 🌙",
    "If you know, you know 🤫",
    "Main kuch nahi bol rahi, bas aankhein bol rahi hain ✨",
    "2 AM rules are always unwritten 🥀",
    "Ek glance hi kafi tha hosh udane ke liye 💋",
    "Don't blame me, blame the vibe 🌙✨",
    "Raat gehri, baatein ankahi... 🌙🖤",
]

# Curated high-reach hashtags for explore page algorithms
GENERAL_HASHTAGS: List[str] = [
    "#nightthought", "#night_thought_12", "#latenightthoughts", "#shayari",
    "#hindishayari", "#poetry", "#reels", "#explorepage", "#viralreels",
    "#trendingreels", "#reelitfeelit", "#fyp", "#foryou", "#explore", "#viral",
    "#instadaily", "#trending", "#reelsinstagram"
]

STYLE_HASHTAGS = {
    "sexy": [
        "#seductivelook", "#latenightvibes", "#flirty", "#desi",
        "#sareelover", "#desiattire", "#indianbeauty", "#moodygrams",
        "#aestheticvibes", "#desiaesthetic", "#boldlook", "#nightowl",
        "#hotanddesi", "#sareebae", "#reelsindia"
    ],
    "broken": [
        "#dard", "#heartbreak", "#brokenheart", "#sadshayari", "#shayari",
        "#latenightthoughts", "#alone", "#feelings", "#sadfeelings",
        "#unexpressedfeelings", "#nightthought", "#alonesad", "#mohabbat"
    ],
    "romantic": [
        "#romanticvibes", "#lovequotes", "#romance", "#feelings",
        "#deepthoughts", "#couplesgoals", "#soulmate", "#aesthetic",
        "#emotionalquotes", "#silentlove", "#ishq", "#pyaar"
    ],
    "traditional": [
        "#saree", "#sareelover", "#traditionalwear", "#desigirl",
        "#ethnicgrace", "#jhumka", "#desiaesthetic", "#indianculture",
        "#sareedraping", "#sareelovers", "#desilove"
    ],
    "baddie": [
        "#baddie", "#attitude", "#attitudequeen", "#bosslady",
        "#unbothered", "#savagequotes", "#selflove", "#aestheticbaddie"
    ],
    "cinematic": [
        "#cinematicreels", "#visualart", "#moodyedits", "#filmphotography",
        "#darkaesthetic", "#cinematography", "#aestheticfeed", "#storytelling"
    ],
    "meme": [
        "#relatablememes", "#funnymemes", "#humor", "#memesdaily",
        "#dailymemes", "#indianmemes", "#dankmemes", "#relatable"
    ],
    "quote": [
        "#deepquotes", "#mindset", "#quotestagram", "#dailyquotes",
        "#lifequotes", "#silence", "#wordsofwhiskey", "#innerpeace"
    ],
    "aesthetic": [
        "#aestheticvibes", "#softaesthetic", "#peace", "#visualart",
        "#warmtones", "#moodyaesthetic", "#calm"
    ],
}


def generate_instagram_caption(
    hook_text: str,
    style: str = "sexy",
    custom_tag_count: int = 12,
) -> str:
    """Generate an Instagram-ready caption complete with hook, teaser/debate CTA, and targeted hashtags for @night_thought_12."""
    clean_hook = hook_text.strip()
    style_key = style.lower().strip()

    teaser = random.choice(TEASERS)
    cta = random.choice(CTAS)

    specific_tags = STYLE_HASHTAGS.get(style_key, STYLE_HASHTAGS["sexy"])
    all_tags = list(set(GENERAL_HASHTAGS + specific_tags))
    random.shuffle(all_tags)
    selected_tags = all_tags[:custom_tag_count]
    hashtag_block = " ".join(selected_tags)

    parts = [
        clean_hook,
        "",
        teaser,
        "",
        f"• {cta}",
        "🌙 Follow @night_thought_12 for daily late night thoughts & poetry ✨",
        "",
        ".",
        ".",
        ".",
        hashtag_block
    ]
    return "\n".join(parts)
