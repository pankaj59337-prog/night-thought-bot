"""Bollywood Music Service for Authentic Vocal / Lyrical Reels."""

import logging
import random
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

logger = logging.getLogger(__name__)

BOLLYWOOD_MUSIC_DIR = Path("assets/music/bollywood")

VOCAL_TRACKS: List[Dict[str, Any]] = [
    # --- Classic & Sensual Romance ---
    {
        "id": "pee_loon",
        "file": "pee_loon_vocal.mp3",
        "title": "Pee Loon",
        "artist": "Mohit Chauhan",
        "lyrics": "Pee loon tere neele neele naino se shabnam...",
        "icon": "💋",
        "style_affinity": ["sexy", "cinematic", "romantic"],
    },
    {
        "id": "kesariya",
        "file": "kesariya_vocal.mp3",
        "title": "Kesariya",
        "artist": "Arijit Singh",
        "lyrics": "Kesariya tera ishq hai piya, rang jaaun jo main...",
        "icon": "💖",
        "style_affinity": ["romantic", "quote", "cinematic", "traditional"],
    },
    {
        "id": "apna_bana_le",
        "file": "apna_bana_le_vocal.mp3",
        "title": "Apna Bana Le",
        "artist": "Arijit Singh",
        "lyrics": "Apna bana le piya, dil ke nagar mein shehar...",
        "icon": "✨",
        "style_affinity": ["sexy", "romantic", "cinematic"],
    },
    {
        "id": "raataan_lambiyan",
        "file": "raataan_lambiyan_vocal.mp3",
        "title": "Raataan Lambiyan",
        "artist": "Jubin Nautiyal",
        "lyrics": "Teri galliyan, raataan lambiyan lambiyan re...",
        "icon": "🌙",
        "style_affinity": ["romantic", "cinematic", "sexy"],
    },
    {
        "id": "o_maahi",
        "file": "o_maahi_vocal.mp3",
        "title": "O Maahi",
        "artist": "Arijit Singh",
        "lyrics": "O maahi re, o maahi re, tere sang ishq kiya...",
        "icon": "🎬",
        "style_affinity": ["cinematic", "romantic", "quote", "sexy"],
    },
    {
        "id": "tum_hi_ho",
        "file": "tum_hi_ho_vocal.mp3",
        "title": "Tum Hi Ho",
        "artist": "Arijit Singh",
        "lyrics": "Kyunki tum hi ho, ab tum hi ho, zindagi ab tum hi ho...",
        "icon": "🌹",
        "style_affinity": ["romantic", "quote", "cinematic", "traditional", "sexy"],
    },
    {
        "id": "tum_hi_aana",
        "file": "tum_hi_aana_vocal.mp3",
        "title": "Tum Hi Aana",
        "artist": "Jubin Nautiyal (Marjaavaan)",
        "lyrics": "Tere jaane ka gham aur na aane ka gham, fir zamane ka gham...",
        "icon": "🥀",
        "style_affinity": ["romantic", "cinematic", "quote", "sexy"],
    },
    {
        "id": "channa_mereya",
        "file": "channa_mereya_vocal.mp3",
        "title": "Channa Mereya",
        "artist": "Arijit Singh",
        "lyrics": "Achha chalta hoon, duaon mein yaad rakhna...",
        "icon": "🥀",
        "style_affinity": ["quote", "cinematic", "romantic", "broken"],
    },
    {
        "id": "zara_sa",
        "file": "zara_sa_vocal.mp3",
        "title": "Zara Sa",
        "artist": "KK",
        "lyrics": "Zara sa dil mein de jagah tu, zara sa apna le bana...",
        "icon": "🔥",
        "style_affinity": ["sexy", "romantic", "cinematic"],
    },
    {
        "id": "agar_tum_saath_ho",
        "file": "agar_tum_saath_ho_vocal.mp3",
        "title": "Agar Tum Saath Ho",
        "artist": "Alka Yagnik & Arijit",
        "lyrics": "Pal bhar theher jaao, dil yeh sambhal jaaye...",
        "icon": "🌧️",
        "style_affinity": ["romantic", "cinematic", "quote", "sexy", "broken"],
    },
    {
        "id": "shayad",
        "file": "shayad_vocal.mp3",
        "title": "Shayad",
        "artist": "Arijit Singh",
        "lyrics": "Shayad kabhi na keh sakoon main tumko...",
        "icon": "💫",
        "style_affinity": ["romantic", "quote", "minimal", "cinematic", "sexy"],
    },
    {
        "id": "kal_ho_naa_ho",
        "file": "kal_ho_naa_ho_vocal.mp3",
        "title": "Kal Ho Naa Ho",
        "artist": "Sonu Nigam",
        "lyrics": "Har ghadi badal rahi hai roop zindagi...",
        "icon": "🌅",
        "style_affinity": ["cinematic", "quote", "romantic"],
    },
    {
        "id": "ve_kamleya",
        "file": "ve_kamleya_vocal.mp3",
        "title": "Ve Kamleya",
        "artist": "Arijit Singh",
        "lyrics": "Ve kamleya, ve kamleya, mere naadan dil...",
        "icon": "🕊️",
        "style_affinity": ["romantic", "traditional", "quote"],
    },
    {
        "id": "hasi_ban_gaye",
        "file": "hasi_ban_gaye_vocal.mp3",
        "title": "Hasi Ban Gaye",
        "artist": "Shreya Ghoshal",
        "lyrics": "Haan hasi ban gaye, haan nami ban gaye...",
        "icon": "🌸",
        "style_affinity": ["romantic", "traditional", "minimal"],
    },
    {
        "id": "kaun_tujhe",
        "file": "kaun_tujhe_vocal.mp3",
        "title": "Kaun Tujhe",
        "artist": "Palak Muchhal",
        "lyrics": "Kaun tujhe yoon pyar karega jaise main karti hoon...",
        "icon": "🤍",
        "style_affinity": ["romantic", "traditional", "quote"],
    },
    {
        "id": "bol_do_na_zara",
        "file": "bol_do_na_zara_vocal.mp3",
        "title": "Bol Do Na Zara",
        "artist": "Armaan Malik",
        "lyrics": "Bol do na zara, dil mein jo hai chhipa...",
        "icon": "💌",
        "style_affinity": ["sexy", "romantic", "cinematic"],
    },
    {
        "id": "dil_de_diya_hai",
        "file": "dil_de_diya_hai_vocal.mp3",
        "title": "Dil De Diya Hai",
        "artist": "Anand Raj Anand",
        "lyrics": "Dil de diya hai, jaan tumhe denge...",
        "icon": "💔",
        "style_affinity": ["romantic", "broken", "cinematic", "traditional", "quote"],
    },
    {
        "id": "lut_gaye",
        "file": "lut_gaye_jubin_nautiyal_vocal.mp3",
        "title": "Lut Gaye",
        "artist": "Jubin Nautiyal",
        "lyrics": "Aankh uthi mohabbat ne angrai li, dil ka sauda hua chandi raat mein...",
        "icon": "🥀",
        "style_affinity": ["romantic", "broken", "cinematic", "sexy", "quote"],
    },
    {
        "id": "aarambh",
        "file": "aarambh_slow_normal.mp3",
        "title": "Aarambh Hai Prachand",
        "artist": "Piyush Mishra",
        "lyrics": "Aarambh hai prachand bole mastako ke jhund...",
        "icon": "⚔️",
        "style_affinity": ["cinematic", "motivational", "attitude"],
    },
    {
        "id": "arjan_vailly",
        "file": "arjan_vailly_vocal.mp3",
        "title": "Arjan Vailly",
        "artist": "Bhupinder Babbal",
        "lyrics": "Arjan vailly ne pair jodke gandasi maari...",
        "icon": "⚡",
        "style_affinity": ["action", "baddie", "attitude", "cinematic"],
    },
    {
        "id": "ghamand_kar",
        "file": "ghamand_kar_vocal.mp3",
        "title": "Ghamand Kar",
        "artist": "Sachet Tandon",
        "lyrics": "Ghamand kar, prachand kar, tandav sa yudh kar...",
        "icon": "🔥",
        "style_affinity": ["cinematic", "motivational", "attitude"],
    },
    {
        "id": "sidhu_295",
        "file": "sidhu_295_vocal.mp3",
        "title": "295",
        "artist": "Sidhu Moosewala",
        "lyrics": "Dass kithe keda ethe dharmi reha...",
        "icon": "🎙️",
        "style_affinity": ["baddie", "attitude", "trending"],
    },
    {
        "id": "kgf_toofan",
        "file": "kgf_toofan_vocal.mp3",
        "title": "Toofan KGF 2",
        "artist": "Ravi Basrur",
        "lyrics": "Toofan jo aayega dushman tharayega...",
        "icon": "🌪️",
        "style_affinity": ["action", "cinematic", "motivational", "attitude"],
    },
    {
        "id": "shubh_cheques",
        "file": "shubh_cheques_vocal.mp3",
        "title": "Cheques",
        "artist": "Shubh",
        "lyrics": "Yeah, cheques in the bank, gallan sab khariyaan...",
        "icon": "💰",
        "style_affinity": ["trending", "attitude", "baddie", "cinematic"],
    },

    # --- Sensual & Hot Late Night ---
    {
        "id": "pehle_bhi_main",
        "file": "pehle_bhi_main_vocal.mp3",
        "title": "Pehle Bhi Main",
        "artist": "Vishal Mishra",
        "lyrics": "Pehle bhi main tumse mila hoon, pehli dafa hi milke laga...",
        "icon": "💋",
        "style_affinity": ["sexy", "romantic", "cinematic", "aesthetic"],
    },
    {
        "id": "satranga",
        "file": "satranga_vocal.mp3",
        "title": "Satranga",
        "artist": "Arijit Singh",
        "lyrics": "Aadha aadha hissa jud raha, tere mere ishq ka...",
        "icon": "🌈",
        "style_affinity": ["romantic", "sexy", "cinematic"],
    },
    {
        "id": "labon_ko",
        "file": "labon_ko_vocal.mp3",
        "title": "Labon Ko",
        "artist": "KK",
        "lyrics": "Labon ko labon pe sajao, kya ho tum mujhe ab batao...",
        "icon": "💋",
        "style_affinity": ["sexy", "romantic", "cinematic"],
    },
    {
        "id": "bheegi_bheegi_raaton",
        "file": "bheegi_bheegi_raaton_vocal.mp3",
        "title": "Bheegi Bheegi Raaton Mein",
        "artist": "Adnan Sami",
        "lyrics": "Bheegi bheegi raaton mein, meethi meethi baaton mein...",
        "icon": "🌧️",
        "style_affinity": ["sexy", "romantic", "aesthetic"],
    },
    {
        "id": "aa_zara",
        "file": "aa_zara_vocal.mp3",
        "title": "Aa Zara",
        "artist": "Sunidhi Chauhan",
        "lyrics": "Aa zara kareeb se, jo pal mile naseeb se...",
        "icon": "🔥",
        "style_affinity": ["sexy", "baddie", "cinematic"],
    },
    {
        "id": "ang_laga_de",
        "file": "ang_laga_de_vocal.mp3",
        "title": "Ang Laga De",
        "artist": "Aditi Paul",
        "lyrics": "Ang laga de re mohe rang laga de re...",
        "icon": "🔥",
        "style_affinity": ["sexy", "romantic", "traditional"],
    },
    {
        "id": "besharam_rang",
        "file": "besharam_rang_vocal.mp3",
        "title": "Besharam Rang",
        "artist": "Shilpa Rao",
        "lyrics": "Humein toh loot liya milke ishq walon ne...",
        "icon": "💃",
        "style_affinity": ["sexy", "baddie", "trending"],
    },
    {
        "id": "aaj_phir_tumpe",
        "file": "aaj_phir_tumpe_vocal.mp3",
        "title": "Aaj Phir Tumpe Pyar",
        "artist": "Arijit Singh",
        "lyrics": "Aaj phir tumpe pyar aaya hai, behad aur beshumar aaya hai...",
        "icon": "🌹",
        "style_affinity": ["sexy", "romantic", "cinematic"],
    },
    {
        "id": "jaadu_hai_nasha",
        "file": "jaadu_hai_nasha_vocal.mp3",
        "title": "Jaadu Hai Nasha Hai",
        "artist": "Shreya Ghoshal",
        "lyrics": "Jaadu hai nasha hai, madhoshian, tujhko bhula ke kahan jaaun main...",
        "icon": "🍷",
        "style_affinity": ["sexy", "romantic", "cinematic"],
    },
    {
        "id": "bakhuda_tumhi_ho",
        "file": "bakhuda_tumhi_ho_vocal.mp3",
        "title": "Bakhuda Tumhi Ho",
        "artist": "Atif Aslam",
        "lyrics": "Bakhuda tumhi ho, har jagah tumhi ho...",
        "icon": "💫",
        "style_affinity": ["romantic", "sexy", "cinematic"],
    },
    {
        "id": "tere_hawaale",
        "file": "tere_hawaale_vocal.mp3",
        "title": "Tere Hawaale",
        "artist": "Arijit Singh & Shilpa Rao",
        "lyrics": "Mera safar chalta raha tere hawaale, tu hi mera sahara...",
        "icon": "🕊️",
        "style_affinity": ["romantic", "quote", "cinematic"],
    },
    {
        "id": "haye_rama",
        "file": "haye_rama_vocal.mp3",
        "title": "Haye Rama",
        "artist": "Hariharan & Swarnalatha",
        "lyrics": "Haye rama yeh kya hua, kyun aise tadpane laga...",
        "icon": "🥀",
        "style_affinity": ["sexy", "romantic", "traditional"],
    },
    {
        "id": "sukoon_mila",
        "file": "sukoon_mila_vocal.mp3",
        "title": "Sukoon Mila",
        "artist": "Arijit Singh",
        "lyrics": "Mila hoon ab jo tum se, hai dil ko mere qasam se sukoon mila...",
        "icon": "🤍",
        "style_affinity": ["romantic", "aesthetic", "cinematic"],
    },
    {
        "id": "tu_jaane_na",
        "file": "tu_jaane_na_vocal.mp3",
        "title": "Tu Jaane Na",
        "artist": "Atif Aslam",
        "lyrics": "Kaise bataaye kyun tujhko chahe, yaara bata na paaye...",
        "icon": "💌",
        "style_affinity": ["romantic", "broken", "cinematic"],
    },
    {
        "id": "teri_jhuki_nazar",
        "file": "teri_jhuki_nazar_vocal.mp3",
        "title": "Teri Jhuki Nazar",
        "artist": "Shafqat Amanat Ali",
        "lyrics": "Chahe kuch na kehna, bhale chup tu rehna...",
        "icon": "👁️",
        "style_affinity": ["sexy", "romantic", "cinematic"],
    },
    {
        "id": "tum_se_hi",
        "file": "tum_se_hi_vocal.mp3",
        "title": "Tum Se Hi",
        "artist": "Mohit Chauhan",
        "lyrics": "Tum se hi din hota hai, surmayi shaam aati hai...",
        "icon": "☀️",
        "style_affinity": ["romantic", "aesthetic", "cinematic"],
    },
    {
        "id": "hawayein",
        "file": "hawayein_vocal.mp3",
        "title": "Hawayein",
        "artist": "Arijit Singh",
        "lyrics": "Hawaayein hawaayein, le jaayein tujhe kahan...",
        "icon": "🍃",
        "style_affinity": ["romantic", "aesthetic", "cinematic"],
    },
    {
        "id": "khuda_jaane",
        "file": "khuda_jaane_vocal.mp3",
        "title": "Khuda Jaane",
        "artist": "KK & Shilpa Rao",
        "lyrics": "Khuda jaane ke main fida hoon, khuda jaane yeh khwaab hai ya haqeeqat...",
        "icon": "🌊",
        "style_affinity": ["romantic", "sexy", "cinematic"],
    },
    {
        "id": "subhanallah",
        "file": "subhanallah_vocal.mp3",
        "title": "Subhanallah",
        "artist": "Sreerama Chandra",
        "lyrics": "Subhanallah, jo ho raha hai pehli dafa hai...",
        "icon": "✨",
        "style_affinity": ["romantic", "aesthetic", "quote"],
    },
    {
        "id": "jalebi_baby",
        "file": "jalebi_baby_vocal.mp3",
        "title": "Jalebi Baby",
        "artist": "Tesher",
        "lyrics": "Baby let me see it, jalebi baby...",
        "icon": "🍯",
        "style_affinity": ["baddie", "sexy", "trending"],
    },

    # --- Midnight Romance & Soulful Love ---
    {
        "id": "o_sajni_re",
        "file": "o_sajni_re_vocal.mp3",
        "title": "O Sajni Re",
        "artist": "Arijit Singh",
        "lyrics": "O sajni re, kaise kate din raat, kaise sahoon yeh doori...",
        "icon": "🌸",
        "style_affinity": ["romantic", "traditional", "quote", "aesthetic"],
    },
    {
        "id": "heeriye",
        "file": "heeriye_vocal.mp3",
        "title": "Heeriye",
        "artist": "Jasleen Royal & Arijit Singh",
        "lyrics": "Heeriye heeriye aa, aaja ve dilon ke shehar mein...",
        "icon": "💫",
        "style_affinity": ["romantic", "aesthetic", "trending"],
    },
    {
        "id": "tera_ban_jaunga",
        "file": "tera_ban_jaunga_vocal.mp3",
        "title": "Tera Ban Jaunga",
        "artist": "Akhil Sachdeva & Tulsi Kumar",
        "lyrics": "Meri raahein tere tak hain, tujhpe hi toh mera haq hai...",
        "icon": "💍",
        "style_affinity": ["romantic", "quote", "cinematic"],
    },
    {
        "id": "pal_ek_pal",
        "file": "pal_ek_pal_vocal.mp3",
        "title": "Pal",
        "artist": "Arijit Singh & Shreya Ghoshal",
        "lyrics": "Pal ek pal mein hi tham sa gaya, tu haath mein haath jo de gaya...",
        "icon": "⏳",
        "style_affinity": ["romantic", "cinematic", "sexy"],
    },
    {
        "id": "zaalima",
        "file": "zaalima_vocal.mp3",
        "title": "Zaalima",
        "artist": "Arijit Singh & Harshdeep Kaur",
        "lyrics": "Jo teri khatir tadpe pehle se hi, usse kya tadpana o zaalima...",
        "icon": "🔥",
        "style_affinity": ["romantic", "sexy", "cinematic"],
    },
    {
        "id": "mast_magan",
        "file": "mast_magan_vocal.mp3",
        "title": "Mast Magan",
        "artist": "Arijit Singh",
        "lyrics": "Ishq ki dhooni roz jalaaye, uthta hai dhuaan toofani sa...",
        "icon": "🪔",
        "style_affinity": ["romantic", "traditional", "cinematic"],
    },
    {
        "id": "pehli_nazar_mein",
        "file": "pehli_nazar_mein_vocal.mp3",
        "title": "Pehli Nazar Mein",
        "artist": "Atif Aslam",
        "lyrics": "Pehli nazar mein kaisa jaadu kar diya, tera ban baitha hai mera jiya...",
        "icon": "⚡",
        "style_affinity": ["romantic", "sexy", "cinematic"],
    },
    {
        "id": "dekha_hazaro_dafa",
        "file": "dekha_hazaro_dafa_vocal.mp3",
        "title": "Dekha Hazaro Dafaa",
        "artist": "Arijit Singh & Palak Muchhal",
        "lyrics": "Dekha hazaro dafaa aapko, phir beqarari kaisi hai...",
        "icon": "👀",
        "style_affinity": ["romantic", "aesthetic", "quote"],
    },
    {
        "id": "soniyo",
        "file": "soniyo_vocal.mp3",
        "title": "Soniyo",
        "artist": "Sonu Nigam & Shreya Ghoshal",
        "lyrics": "Soniyo o soniyo, tumhein dekhta hoon toh lagta hai jaise...",
        "icon": "💖",
        "style_affinity": ["romantic", "quote", "cinematic"],
    },
    {
        "id": "tujh_mein_rab",
        "file": "tujh_mein_rab_vocal.mp3",
        "title": "Tujh Mein Rab Dikhta Hai",
        "artist": "Roop Kumar Rathod",
        "lyrics": "Tujh mein rab dikhta hai yaara main kya karoon...",
        "icon": "🙏",
        "style_affinity": ["romantic", "traditional", "quote"],
    },
    {
        "id": "ishq_wala_love",
        "file": "ishq_wala_love_vocal.mp3",
        "title": "Ishq Wala Love",
        "artist": "Shekhar Ravjiani & Neeti Mohan",
        "lyrics": "Suraj hua maddham, chaand dhalne laga, ishq wala love...",
        "icon": "🧡",
        "style_affinity": ["romantic", "aesthetic", "minimal"],
    },
    {
        "id": "samjhawan",
        "file": "samjhawan_vocal.mp3",
        "title": "Samjhawan",
        "artist": "Arijit Singh & Shreya Ghoshal",
        "lyrics": "Main tenu samjhawan ki, na tere bina lagda ji...",
        "icon": "🥀",
        "style_affinity": ["romantic", "traditional", "quote"],
    },
    {
        "id": "jeena_jeena",
        "file": "jeena_jeena_vocal.mp3",
        "title": "Jeena Jeena",
        "artist": "Atif Aslam",
        "lyrics": "Dehleez pe mere dil ki jo rakhe hain tune kadam...",
        "icon": "🕊️",
        "style_affinity": ["romantic", "cinematic", "aesthetic"],
    },
    {
        "id": "raabta",
        "file": "raabta_vocal.mp3",
        "title": "Raabta",
        "artist": "Arijit Singh",
        "lyrics": "Kehte hain khuda ne iss jahan mein sabhi ke liye kisi na kisi ko hai banaya...",
        "icon": "🌌",
        "style_affinity": ["romantic", "cinematic", "aesthetic"],
    },
    {
        "id": "banjaara",
        "file": "banjaara_vocal.mp3",
        "title": "Banjaara",
        "artist": "Mohammed Irfan",
        "lyrics": "Jise zindagi dhoondh rahi hai, kya ye woh makaam mera hai...",
        "icon": "🎒",
        "style_affinity": ["romantic", "cinematic", "broken"],
    },
    {
        "id": "nazm_nazm",
        "file": "nazm_nazm_vocal.mp3",
        "title": "Nazm Nazm",
        "artist": "Ayushmann Khurrana",
        "lyrics": "Tu nazm nazm sa mere honthon pe thehar ja...",
        "icon": "📜",
        "style_affinity": ["romantic", "aesthetic", "quote"],
    },
    {
        "id": "duniyaa",
        "file": "duniyaa_vocal.mp3",
        "title": "Duniyaa",
        "artist": "Akhil & Dhvani Bhanushali",
        "lyrics": "Bulave tujhe yaar aaj meri galiyan, basau tere sang main alag duniya...",
        "icon": "🌍",
        "style_affinity": ["romantic", "trending", "aesthetic"],
    },
    {
        "id": "tere_sang_yaara",
        "file": "tere_sang_yaara_vocal.mp3",
        "title": "Tere Sang Yaara",
        "artist": "Atif Aslam",
        "lyrics": "Tere sang yaara, khush rang bahara, tu raat deewani main zard sitara...",
        "icon": "⭐",
        "style_affinity": ["romantic", "cinematic", "aesthetic"],
    },
    {
        "id": "chal_wahan_jaate_hain",
        "file": "chal_wahan_jaate_hain_vocal.mp3",
        "title": "Chal Wahan Jaate Hain",
        "artist": "Arijit Singh",
        "lyrics": "Aasmaan ke pare ek jahaan hai kahin, chal wahan jaate hain...",
        "icon": "☁️",
        "style_affinity": ["romantic", "cinematic", "aesthetic"],
    },
    {
        "id": "ishq_sufiyana",
        "file": "ishq_sufiyana_vocal.mp3",
        "title": "Ishq Sufiyana",
        "artist": "Kamal Khan",
        "lyrics": "Rab ki nemat hai teri nigahein, rab ka deedar hai tera chehra...",
        "icon": "💫",
        "style_affinity": ["romantic", "traditional", "cinematic"],
    },

    # --- Broken Heart, Dard & Late Night Sad ---
    {
        "id": "bekhayali",
        "file": "bekhayali_vocal.mp3",
        "title": "Bekhayali",
        "artist": "Sachet Tandon",
        "lyrics": "Bekhayali mein bhi tera hi khayal aaye, kyun bichhadna hai zaroori...",
        "icon": "💔",
        "style_affinity": ["broken", "cinematic", "quote", "attitude"],
    },
    {
        "id": "thodi_jagah",
        "file": "thodi_jagah_vocal.mp3",
        "title": "Thodi Jagah",
        "artist": "Arijit Singh",
        "lyrics": "Thodi jagah de de mujhe tere paas kahin reh jaaun main...",
        "icon": "🥀",
        "style_affinity": ["broken", "romantic", "cinematic"],
    },
    {
        "id": "hamari_adhuri_kahani",
        "file": "hamari_adhuri_kahani_vocal.mp3",
        "title": "Hamari Adhuri Kahani",
        "artist": "Arijit Singh",
        "lyrics": "Khushbu se teri yunhi takra gaye, chalte chalte hum kahan aa gaye...",
        "icon": "🌧️",
        "style_affinity": ["broken", "romantic", "cinematic"],
    },
    {
        "id": "bhula_dena",
        "file": "bhula_dena_vocal.mp3",
        "title": "Bhula Dena Mujhe",
        "artist": "Mustafa Zahid",
        "lyrics": "Bhula dena mujhe, hai alvida tujhe, tujhe jeena hai mere bina...",
        "icon": "🚪",
        "style_affinity": ["broken", "cinematic", "quote"],
    },
    {
        "id": "tujhe_kitna_chahne_lage",
        "file": "tujhe_kitna_chahne_lage_vocal.mp3",
        "title": "Tujhe Kitna Chahne Lage",
        "artist": "Arijit Singh",
        "lyrics": "Dil ka dariya beh hi gaya, ishq ibadat ban hi gaya...",
        "icon": "🌊",
        "style_affinity": ["broken", "romantic", "cinematic"],
    },
    {
        "id": "phir_bhi_tumko_chahunga",
        "file": "phir_bhi_tumko_chahunga_vocal.mp3",
        "title": "Phir Bhi Tumko Chahunga",
        "artist": "Arijit Singh",
        "lyrics": "Main phir bhi tumko chahunga, iss chaahat mein mar jaaunga...",
        "icon": "🖤",
        "style_affinity": ["broken", "romantic", "cinematic"],
    },
    {
        "id": "judaai",
        "file": "judaai_vocal.mp3",
        "title": "Judaai",
        "artist": "Rekha Bhardwaj & Arijit Singh",
        "lyrics": "Chhad gaya ve jeene da sahara, judaai das kiven sahan...",
        "icon": "🥀",
        "style_affinity": ["broken", "cinematic", "traditional"],
    },
    {
        "id": "main_dhoondne",
        "file": "main_dhoondne_vocal.mp3",
        "title": "Main Dhoondne Ko Zamaane Mein",
        "artist": "Arijit Singh",
        "lyrics": "Main dhoondne ko zamaane mein jab wafa nikla...",
        "icon": "🔍",
        "style_affinity": ["broken", "quote", "cinematic"],
    },
    {
        "id": "jag_ghoomeya",
        "file": "jag_ghoomeya_vocal.mp3",
        "title": "Jag Ghoomeya",
        "artist": "Rahat Fateh Ali Khan",
        "lyrics": "Maine jag ghoomeya thare jaisa na koi...",
        "icon": "🌍",
        "style_affinity": ["romantic", "traditional", "quote"],
    },
    {
        "id": "tera_chehra",
        "file": "tera_chehra_vocal.mp3",
        "title": "Tera Chehra",
        "artist": "Arijit Singh",
        "lyrics": "Meri bechainiyon ko chain mil jaaye, tera chehra jab nazar aaye...",
        "icon": "🌙",
        "style_affinity": ["broken", "romantic", "cinematic"],
    },
    {
        "id": "sanam_teri_kasam",
        "file": "sanam_teri_kasam_vocal.mp3",
        "title": "Sanam Teri Kasam",
        "artist": "Ankit Tiwari & Palak Muchhal",
        "lyrics": "Sar jhukaaye main sochta hoon, kyun tu juda hua...",
        "icon": "🥀",
        "style_affinity": ["broken", "romantic", "cinematic"],
    },
    {
        "id": "maana_dil",
        "file": "maana_dil_vocal.mp3",
        "title": "Maana Dil",
        "artist": "B Praak",
        "lyrics": "Maana dil dara dara hai, toota ye zara zara hai...",
        "icon": "💔",
        "style_affinity": ["broken", "quote", "cinematic"],
    },
    {
        "id": "rula_ke_gaya",
        "file": "rula_ke_gaya_vocal.mp3",
        "title": "Rula Ke Gaya Ishq Tera",
        "artist": "Stebin Ben",
        "lyrics": "Rula ke gaya ishq tera, dil tod ke gaya ishq tera...",
        "icon": "💧",
        "style_affinity": ["broken", "quote", "aesthetic"],
    },
    {
        "id": "qismat",
        "file": "qismat_vocal.mp3",
        "title": "Qismat",
        "artist": "Ammy Virk",
        "lyrics": "Je main nahi tere kol te phir kaun hoyega...",
        "icon": "🥀",
        "style_affinity": ["broken", "quote", "cinematic"],
    },
    {
        "id": "filhall",
        "file": "filhall_vocal.mp3",
        "title": "Filhall",
        "artist": "B Praak",
        "lyrics": "Main kisi aur ka hoon filhall ke tera ho jaaun...",
        "icon": "🩹",
        "style_affinity": ["broken", "romantic", "cinematic"],
    },

    # --- Viral Indie, Lo-Fi & Aesthetic Hooks ---
    {
        "id": "tu_hai_kahan",
        "file": "tu_hai_kahan_vocal.mp3",
        "title": "Tu Hai Kahan",
        "artist": "AUR",
        "lyrics": "Tu hai kahan, khwaabon ke iss jahaan mein...",
        "icon": "🌙",
        "style_affinity": ["aesthetic", "romantic", "trending"],
    },
    {
        "id": "choo_lo",
        "file": "choo_lo_vocal.mp3",
        "title": "Choo Lo",
        "artist": "The Local Train",
        "lyrics": "Khada hoon aaj bhi wahin, ke dil phir beqarar hai...",
        "icon": "🚂",
        "style_affinity": ["aesthetic", "broken", "quote"],
    },
    {
        "id": "aaoge_tum_kabhi",
        "file": "aaoge_tum_kabhi_vocal.mp3",
        "title": "Aaoge Tum Kabhi",
        "artist": "The Local Train",
        "lyrics": "Aaoge tum kabhi, meri jaan keh rahi...",
        "icon": "⏳",
        "style_affinity": ["aesthetic", "romantic", "cinematic"],
    },
    {
        "id": "alag_aasman",
        "file": "alag_aasman_vocal.mp3",
        "title": "Alag Aasman",
        "artist": "Anuv Jain",
        "lyrics": "Naye shehar mein naye log hain, par dil mein tu hi rehti hai...",
        "icon": "☁️",
        "style_affinity": ["aesthetic", "romantic", "quote"],
    },
    {
        "id": "baarishein",
        "file": "baarishein_vocal.mp3",
        "title": "Baarishein",
        "artist": "Anuv Jain",
        "lyrics": "Hawaayein rang badal rahi hain, ghaat pe baitha main soch raha...",
        "icon": "🌧️",
        "style_affinity": ["aesthetic", "romantic", "minimal"],
    },
    {
        "id": "husn",
        "file": "husn_vocal.mp3",
        "title": "Husn",
        "artist": "Anuv Jain",
        "lyrics": "Dekho dekho kaisi baatein yahan ki, husn tera aisi raat mein...",
        "icon": "✨",
        "style_affinity": ["aesthetic", "sexy", "trending", "romantic"],
    },
    {
        "id": "jo_tum_mere_ho",
        "file": "jo_tum_mere_ho_vocal.mp3",
        "title": "Jo Tum Mere Ho",
        "artist": "Anuv Jain",
        "lyrics": "Jo tum mere ho toh kya gham hai, duniya ruthe toh kya...",
        "icon": "🤍",
        "style_affinity": ["aesthetic", "romantic", "trending"],
    },
    {
        "id": "gul",
        "file": "gul_vocal.mp3",
        "title": "Gul",
        "artist": "Anuv Jain",
        "lyrics": "Tu dhoop jaisi nikalti hai jahan, gul khil jaate hain wahan...",
        "icon": "🌻",
        "style_affinity": ["aesthetic", "romantic", "minimal"],
    },
    {
        "id": "faasle",
        "file": "faasle_vocal.mp3",
        "title": "Faasle",
        "artist": "Aditya Rikhari",
        "lyrics": "Yeh faasle jo darmiyaan hain, mita do na aakar...",
        "icon": "🕯️",
        "style_affinity": ["aesthetic", "romantic", "broken"],
    },
    {
        "id": "samjho_na",
        "file": "samjho_na_vocal.mp3",
        "title": "Samjho Na",
        "artist": "Aditya Rikhari",
        "lyrics": "Samjho na kuch toh samjho na, dil ka haal suno zara...",
        "icon": "🎧",
        "style_affinity": ["aesthetic", "romantic", "trending"],
    },
    {
        "id": "kahani_suno",
        "file": "kahani_suno_vocal.mp3",
        "title": "Kahani Suno 2.0",
        "artist": "Kaifi Khalil",
        "lyrics": "Mujhe pyaar hua tha, ikraar hua tha...",
        "icon": "🥀",
        "style_affinity": ["broken", "aesthetic", "romantic", "trending"],
    },
    {
        "id": "kasoor",
        "file": "kasoor_vocal.mp3",
        "title": "Kasoor",
        "artist": "Prateek Kuhad",
        "lyrics": "Yeh mera kasoor hai ke main tujhe chahta hoon...",
        "icon": "💌",
        "style_affinity": ["aesthetic", "romantic", "minimal"],
    },
    {
        "id": "cold_mess",
        "file": "cold_mess_vocal.mp3",
        "title": "Cold/Mess",
        "artist": "Prateek Kuhad",
        "lyrics": "When I feel cold, I keep you close...",
        "icon": "❄️",
        "style_affinity": ["aesthetic", "romantic", "sexy"],
    },
    {
        "id": "kho_gaye_hum",
        "file": "kho_gaye_hum_vocal.mp3",
        "title": "Kho Gaye Hum Kahan",
        "artist": "Jasleen Royal & Prateek Kuhad",
        "lyrics": "Kho gaye hum kahan, rangon sa yeh jahaan...",
        "icon": "🎈",
        "style_affinity": ["aesthetic", "romantic", "minimal"],
    },
    {
        "id": "iktara",
        "file": "iktara_vocal.mp3",
        "title": "Iktara",
        "artist": "Kavita Seth & Amit Trivedi",
        "lyrics": "Goonja sa koi iktara iktara, goonja sa koi iktara...",
        "icon": "🪕",
        "style_affinity": ["aesthetic", "romantic", "traditional"],
    },
    {
        "id": "kabira",
        "file": "kabira_vocal.mp3",
        "title": "Kabira",
        "artist": "Tochi Raina & Rekha Bhardwaj",
        "lyrics": "Banno re banno meri chali sasuraal ko, ankhiyon mein paani...",
        "icon": "🕊️",
        "style_affinity": ["aesthetic", "quote", "traditional"],
    },
    {
        "id": "soulmate",
        "file": "soulmate_vocal.mp3",
        "title": "Soulmate",
        "artist": "Badshah & Arijit Singh",
        "lyrics": "Bheegi bheegi raaton mein aaja, tu mera soulmate hai...",
        "icon": "💑",
        "style_affinity": ["romantic", "sexy", "trending"],
    },

    # --- Baddie, Attitude, Punjabi Late Night & Swag ---
    {
        "id": "with_you",
        "file": "with_you_vocal.mp3",
        "title": "With You",
        "artist": "AP Dhillon",
        "lyrics": "Tere naal hi rehna ji, tere bin nahi jeena...",
        "icon": "🏖️",
        "style_affinity": ["aesthetic", "romantic", "baddie", "trending"],
    },
    {
        "id": "dil_nu",
        "file": "dil_nu_vocal.mp3",
        "title": "Dil Nu",
        "artist": "AP Dhillon",
        "lyrics": "Dil nu tere naal pyaar bada hai, kardi kyon inkaar...",
        "icon": "❤️‍🔥",
        "style_affinity": ["baddie", "romantic", "trending"],
    },
    {
        "id": "excuses",
        "file": "excuses_vocal.mp3",
        "title": "Excuses",
        "artist": "AP Dhillon & Gurinder Gill",
        "lyrics": "Kehndi hundi si chan tak raah bana de...",
        "icon": "🌙",
        "style_affinity": ["baddie", "broken", "trending", "attitude"],
    },
    {
        "id": "summer_high",
        "file": "summer_high_vocal.mp3",
        "title": "Summer High",
        "artist": "AP Dhillon",
        "lyrics": "Lagdi mainu tu summer high wargi...",
        "icon": "☀️",
        "style_affinity": ["baddie", "sexy", "trending"],
    },
    {
        "id": "brown_munde",
        "file": "brown_munde_vocal.mp3",
        "title": "Brown Munde",
        "artist": "AP Dhillon & Gurinder Gill",
        "lyrics": "Desi jehe geet aa trap munde, brown munde...",
        "icon": "🧢",
        "style_affinity": ["baddie", "attitude", "trending"],
    },
    {
        "id": "baller",
        "file": "baller_vocal.mp3",
        "title": "Baller",
        "artist": "Shubh",
        "lyrics": "Baller wangu life jiyonde munde, cheques in the bank...",
        "icon": "🏀",
        "style_affinity": ["baddie", "attitude", "trending"],
    },
    {
        "id": "one_love",
        "file": "one_love_vocal.mp3",
        "title": "One Love",
        "artist": "Shubh",
        "lyrics": "One love, baby girl give me one love...",
        "icon": "❤️",
        "style_affinity": ["baddie", "romantic", "trending"],
    },
    {
        "id": "elevated",
        "file": "elevated_vocal.mp3",
        "title": "Elevated",
        "artist": "Shubh",
        "lyrics": "Asi level up kite saare game ch, elevated...",
        "icon": "🚀",
        "style_affinity": ["baddie", "attitude", "trending"],
    },
    {
        "id": "tauba_tauba",
        "file": "tauba_tauba_vocal.mp3",
        "title": "Tauba Tauba",
        "artist": "Karan Aujla",
        "lyrics": "Husn tera tauba tauba, kardi ae nakhre tauba...",
        "icon": "🕶️",
        "style_affinity": ["baddie", "sexy", "trending"],
    },
    {
        "id": "softly",
        "file": "softly_vocal.mp3",
        "title": "Softly",
        "artist": "Karan Aujla",
        "lyrics": "Tu softly meri gall sun le soniye...",
        "icon": "🧸",
        "style_affinity": ["baddie", "romantic", "sexy", "trending"],
    },
    {
        "id": "winning_speech",
        "file": "winning_speech_vocal.mp3",
        "title": "Winning Speech",
        "artist": "Karan Aujla",
        "lyrics": "Pehle din ton hi likheya naseeb ch victory...",
        "icon": "🏆",
        "style_affinity": ["baddie", "attitude", "motivational"],
    },
    {
        "id": "admirin_you",
        "file": "admirin_you_vocal.mp3",
        "title": "Admirin You",
        "artist": "Karan Aujla & Preston Pablo",
        "lyrics": "Girl I've been admirin' you from afar...",
        "icon": "✨",
        "style_affinity": ["baddie", "romantic", "aesthetic", "trending"],
    },
    {
        "id": "white_brown_black",
        "file": "white_brown_black_vocal.mp3",
        "title": "White Brown Black",
        "artist": "Avvy Sra & Karan Aujla",
        "lyrics": "Kude rang tera white brown black ni...",
        "icon": "🔥",
        "style_affinity": ["baddie", "sexy", "trending"],
    },
    {
        "id": "lover_diljit",
        "file": "lover_diljit_vocal.mp3",
        "title": "Lover",
        "artist": "Diljit Dosanjh",
        "lyrics": "Tera ni lover, tera ni lover, dil mera le gayi...",
        "icon": "💘",
        "style_affinity": ["romantic", "baddie", "trending"],
    },
    {
        "id": "naina_diljit",
        "file": "naina_diljit_vocal.mp3",
        "title": "Naina",
        "artist": "Diljit Dosanjh & Badshah",
        "lyrics": "Naina tere kajrare naina, dil cheen ke le gaye...",
        "icon": "👀",
        "style_affinity": ["baddie", "sexy", "romantic", "trending"],
    },
    {
        "id": "kinni_kinni",
        "file": "kinni_kinni_vocal.mp3",
        "title": "Kinni Kinni",
        "artist": "Diljit Dosanjh",
        "lyrics": "Kinni kinni vaari main tenu dassa...",
        "icon": "💫",
        "style_affinity": ["baddie", "romantic", "trending"],
    },
    {
        "id": "mi_amor",
        "file": "mi_amor_vocal.mp3",
        "title": "Mi Amor",
        "artist": "Sharn & 407",
        "lyrics": "Kudiye ni tere brown rang ne, mi amor...",
        "icon": "🌹",
        "style_affinity": ["baddie", "sexy", "romantic", "trending"],
    },
    {
        "id": "hass_hass",
        "file": "hass_hass_vocal.mp3",
        "title": "Hass Hass",
        "artist": "Diljit Dosanjh & Sia",
        "lyrics": "Kudiye tu hass hass ke dil mangdi...",
        "icon": "😊",
        "style_affinity": ["romantic", "trending", "aesthetic"],
    },
    {
        "id": "gulabi_sadi",
        "file": "gulabi_sadi_vocal.mp3",
        "title": "Gulabi Sadi",
        "artist": "Sanju Rathod",
        "lyrics": "Gulabi sadi aani laali laal laal...",
        "icon": "🥻",
        "style_affinity": ["baddie", "trending", "sexy"],
    },
    {
        "id": "chal_kudiye",
        "file": "chal_kudiye_vocal.mp3",
        "title": "Chal Kudiye",
        "artist": "Alia Bhatt & Diljit Dosanjh",
        "lyrics": "Chal kudiye uth kudiye, ud ja hawa ke sang...",
        "icon": "🦋",
        "style_affinity": ["aesthetic", "trending", "motivational"],
    },
]

TRACK_METADATA: Dict[str, Dict[str, Any]] = {
    t["file"]: {
        "title": f"{t['title']} ({t['artist']} - Vocal)",
        "artist": t["artist"],
        "lyrics": t["lyrics"],
        "style_affinity": t["style_affinity"],
    }
    for t in VOCAL_TRACKS
}


class MusicService:
    """Manages Bollywood vocal soundtrack selection and integration."""

    def __init__(self, music_dir: Path = BOLLYWOOD_MUSIC_DIR):
        self.music_dir = music_dir
        self.music_dir.mkdir(parents=True, exist_ok=True)

    def get_vocal_options(
        self,
        category: Optional[str] = None,
        exclude_ids: Optional[set] = None,
        limit: int = 5,
    ) -> List[Dict[str, Any]]:
        """Return fresh vocal / lyrics Bollywood tracks filtered by category and excluding already used ones."""
        exclude = set(exclude_ids) if exclude_ids else set()

        # Filter by category / style affinity if provided
        cat = category.lower().strip() if category else None
        if cat:
            cat_pool = [
                t for t in VOCAL_TRACKS
                if any(cat in aff.lower() for aff in t.get("style_affinity", []))
                or (cat in ("baddie", "bestie", "aesthetic") and any(aff.lower() in ("sexy", "romantic") for aff in t.get("style_affinity", [])))
                or (cat == "broken" and any(aff.lower() in ("cinematic", "romantic") for aff in t.get("style_affinity", [])))
            ]
            # If category has tracks, use that pool; else fallback to all
            pool = cat_pool if cat_pool else VOCAL_TRACKS
        else:
            pool = VOCAL_TRACKS

        candidates = [t for t in pool if t["id"] not in exclude]
        if not candidates:
            candidates = list(pool)

        # Shuffle candidates for fresh order
        random.shuffle(candidates)
        results = []
        for t in candidates[:limit]:
            path = self.music_dir / t["file"]
            results.append({**t, "path": path})
        return results

    def get_vocal_track_by_id(self, track_id: str) -> Optional[Path]:
        """Find vocal track path by its identifier (e.g. 'pee_loon'). Auto-downloads if not cached."""
        for t in VOCAL_TRACKS:
            if t["id"] == track_id:
                p = self.music_dir / t["file"]
                if p.exists() and p.stat().st_size > 1000:
                    return p
                raw_p = self.music_dir / f"{track_id}_raw.mp3"
                if raw_p.exists() and raw_p.stat().st_size > 1000:
                    return raw_p
                # Auto-download on demand using yt-dlp
                try:
                    logger.info(f"Track '{t['title']}' ({track_id}) not found locally. Auto-fetching online...")
                    downloaded = self._download_online_track(
                        f"{t['title']} {t['artist']}",
                        title_hint=t["title"],
                    )
                    if downloaded and downloaded[0].exists():
                        dl_path = downloaded[0]
                        target_path = self.music_dir / t["file"]
                        if not target_path.exists() and dl_path.exists():
                            try:
                                import shutil
                                shutil.copy2(dl_path, target_path)
                                return target_path
                            except Exception:
                                pass
                        return dl_path
                except Exception as e:
                    logger.warning(f"Could not auto-download track '{t['title']}': {e}")
                break
        return None

    def resolve_song_by_name(self, query: str, category: Optional[str] = None) -> Tuple[Path, str]:
        """Resolve a user-specified song name or URL to an authentic vocal audio track.
        Matches against local library first, then searches & downloads via yt-dlp if needed."""
        import re

        clean_query = query.strip()
        url_match = re.search(r"https?://[^\s)\]]+", clean_query)
        url = url_match.group(0) if url_match else None

        # Clean text without URLs or markdown
        clean_text = re.sub(r"https?://[^\s)\]]+", "", clean_query)
        clean_text = re.sub(r"[\[\]\(\)\"\'\-_]", " ", clean_text)
        clean_text = " ".join(clean_text.split()).strip()
        q_norm = clean_text.lower()

        # If a direct URL was supplied, download/extract from it directly
        if url:
            logger.info(f"Direct song URL provided by user: {url}")
            downloaded = self._download_online_track(url, title_hint=clean_text)
            if downloaded:
                return downloaded

        # 1. Exact or strong substring match in VOCAL_TRACKS
        if q_norm:
            matches = []
            for t in VOCAL_TRACKS:
                t_title = t["title"].lower()
                t_id = t["id"].lower()
                # Exact equality
                if q_norm == t_title or q_norm == t_id:
                    matches.append((100, len(t_title), t))
                # Title is in user query (e.g. "Tum Hi Aana (From Marjaavaan)")
                elif t_title in q_norm or t_id in q_norm:
                    matches.append((50, len(t_title), t))
                # User query is in title
                elif len(q_norm) >= 4 and q_norm in t_title:
                    matches.append((30, len(q_norm), t))

            if matches:
                # Prioritize highest rank and longest matching title
                matches.sort(key=lambda x: (x[0], x[1]), reverse=True)
                best_t = matches[0][2]
                p = self.get_vocal_track_by_id(best_t["id"])
                if p and p.exists():
                    logger.info(f"Matched '{query}' to local track: {best_t['title']}")
                    return p, f"{best_t['title']} ({best_t['artist']})"

        # 2. Check existing local mp3 files in music directory
        if q_norm:
            safe_slug = re.sub(r"[^a-zA-Z0-9_]", "_", q_norm)[:30]
            for p in self.music_dir.glob("*.mp3"):
                stem = p.stem.lower()
                if q_norm in stem or stem in q_norm or safe_slug in stem:
                    return p, self.get_track_title(p)

        # 3. If not in local library, download exact requested song online via yt-dlp
        target_to_search = clean_text or clean_query
        try:
            logger.info(f"Song '{target_to_search}' not in local library. Downloading online via yt-dlp...")
            downloaded = self._download_online_track(target_to_search)
            if downloaded:
                return downloaded
        except Exception as e:
            logger.warning(f"Online song fetch failed for '{target_to_search}': {e}")

        # 4. Fallback to style-matched track from library only if download fails
        fallback = self.get_bollywood_track(category or "romantic")
        return fallback, self.get_track_title(fallback)

    def _download_online_track(self, query: str, title_hint: Optional[str] = None) -> Optional[Tuple[Path, str]]:
        """Download and trim a 16s chorus clip from YouTube or JioSaavn using yt-dlp."""
        import subprocess
        import re

        clean_q = query.strip()
        is_url = clean_q.startswith("http://") or clean_q.startswith("https://")

        if is_url:
            target = clean_q
            if "jiosaavn.com" in target and "/lyrics/" in target:
                # Convert JioSaavn lyrics URL to song URL for yt-dlp extractor
                target = target.replace("/lyrics/", "/song/").replace("-lyrics/", "/")
            slug = re.sub(r"[^a-zA-Z0-9_]", "", target.split("/")[-1])[:30] or "saavn_track"
        else:
            target = f"ytsearch1:{clean_q} song audio"
            slug = re.sub(r"[^a-zA-Z0-9_]", "_", clean_q.lower())[:30]

        out_raw = self.music_dir / f"{slug}_raw.mp3"
        out_vocal = self.music_dir / f"{slug}_vocal.mp3"

        if out_vocal.exists() and out_vocal.stat().st_size > 1000:
            display_title = title_hint.title() if title_hint else clean_q.title()
            return out_vocal, f"{display_title} (Vocal Chorus)"

        targets_to_try = [target]
        if not is_url:
            targets_to_try.append(f"scsearch1:{clean_q}")

        for current_target in targets_to_try:
            logger.info(f"Running yt-dlp for target: {current_target}")
            cmd = [
                "yt-dlp",
                "--extract-audio",
                "--audio-format", "mp3",
                "--output", str(out_raw),
                "--max-filesize", "25M",
                "--no-playlist",
            ]
            if "ytsearch" in current_target or "youtube" in current_target:
                cmd.extend(["--extractor-args", "youtube:player_client=android"])
            cmd.append(current_target)

            res = subprocess.run(cmd, capture_output=True, text=True, timeout=45)
            if res.returncode == 0 and out_raw.exists() and out_raw.stat().st_size > 1000:
                # Get video/song title
                title_cmd = ["yt-dlp", "--get-title", "--no-playlist", current_target]
                t_res = subprocess.run(title_cmd, capture_output=True, text=True, timeout=15)
                extracted_title = (
                    t_res.stdout.strip()
                    if t_res.returncode == 0 and t_res.stdout.strip()
                    else (title_hint.title() if title_hint else clean_q.title())
                )
                clean_display = extracted_title.split("|")[0].split("(")[0].strip() if "|" in extracted_title else extracted_title

                # Cut 16s high-energy chorus clip with FFmpeg (start at 30s)
                trim_cmd = [
                    "ffmpeg", "-y",
                    "-ss", "00:00:30",
                    "-i", str(out_raw),
                    "-t", "16",
                    "-c", "copy",
                    str(out_vocal),
                ]
                subprocess.run(trim_cmd, capture_output=True, timeout=15)
                if out_vocal.exists() and out_vocal.stat().st_size > 1000:
                    return out_vocal, f"{clean_display} (Vocal Chorus)"
                return out_raw, f"{clean_display} (Vocal Chorus)"
            else:
                logger.warning(f"Target '{current_target}' failed ({res.returncode}): {res.stderr[:160] if res.stderr else 'no output'}")

        return None

    def get_available_tracks(self) -> List[Path]:
        """List valid MP3 files in the Bollywood music library (prioritizing vocal tracks)."""
        if not self.music_dir.exists():
            return []
        vocals = [p for p in self.music_dir.glob("*_vocal.mp3") if p.stat().st_size > 1000]
        if vocals:
            return vocals
        return [p for p in self.music_dir.glob("*.mp3") if p.stat().st_size > 1000]

    def get_bollywood_track(self, style: Optional[str] = None) -> Optional[Path]:
        """Select a Bollywood vocal track, matching the given reel style if possible."""
        tracks = self.get_available_tracks()
        if not tracks:
            fallback = Path("data/audio/sensual_ambient.mp3")
            return fallback if fallback.exists() else None

        if style:
            style_lower = style.lower().strip()
            candidates = [
                p for p in tracks
                if p.name in TRACK_METADATA and (
                    style_lower in TRACK_METADATA[p.name].get("style_affinity", [])
                    or (style_lower in ("baddie", "bestie", "aesthetic") and any(s in TRACK_METADATA[p.name].get("style_affinity", []) for s in ["sexy", "romantic"]))
                    or (style_lower == "broken" and any(s in TRACK_METADATA[p.name].get("style_affinity", []) for s in ["cinematic", "romantic"]))
                )
            ]
            if candidates:
                chosen = random.choice(candidates)
                logger.info(f"Selected style-matched vocal track: {chosen.name} for style '{style}'")
                return chosen

        chosen = random.choice(tracks)
        logger.info(f"Selected random vocal track: {chosen.name}")
        return chosen

    def get_track_title(self, path: Optional[Path]) -> str:
        """Return human-friendly display name of the track."""
        if not path:
            return "Bollywood Vocal Track"
        filename = path.name
        if filename in TRACK_METADATA:
            return TRACK_METADATA[filename]["title"]
        clean = (
            path.stem.replace("_vocal", "")
            .replace("_raw", "")
            .replace("_lofi", "")
            .replace("_", " ")
            .title()
        )
        return f"{clean} (Vocal Lyrics)"


music_service = MusicService()


