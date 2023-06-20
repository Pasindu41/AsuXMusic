from os import getenv

from dotenv import load_dotenv

load_dotenv()

admins = {}

SESSION_NAME = getenv("SESSION_NAME", "BQAg8WhSCh3g0fwNTHN-8Qt1sJGT_IUTNcI9yOnMpCv80cCw5XUHeP4QwXXLs3q5kcSyMQQ-thlVEzxrVid5lAsIbN6GM6JrnIVsYrsAp9OaSmA3ScJgPnGxpzUV7DkzVPr1MgwGRsXMQK08z52ZvbfXnbHCda9GydwcZ_0-JRnlsScreWpDVu6Sb7ODa7ps4y7XX7ELzyP7b0DvoEpVoDIL7wfSVQz_iz1m8xibpwgHcInnIl5CDr1Vjad_yNzQk6OZDJpwG_qtYoZXuS-bBYho0bHhablbS8_mJPHrif7UuyruGJPOlYeRRFnJYOzeEURby6B-VBGjz1hNpya7EASuAAAAAWxij1EA")

BOT_TOKEN = getenv("BOT_TOKEN", "5904474622:AAFaLWpKVj-vAxONTXat7c7mWfGYivNjxXY")
API_ID = int(getenv("API_ID", "27467283"))
API_HASH = getenv("API_HASH", "33b272caee9a0d79537cad6b6f33b3f7")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "sri_lankan_dark_Angels_2023")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "sri_lankan_dark_Angels_2023")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5975259062").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5975259062").split()))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))

IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/31e9ecee16a46575267a4.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/d744707634106cf76627a.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/d8f8fc1de9110b93ca94c.jpg")
YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL", "https://te.legra.ph/file/bc5556476395a0c8e109b.jpg"
)
