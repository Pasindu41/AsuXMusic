from os import getenv

from dotenv import load_dotenv

load_dotenv()

admins = {}

SESSION_NAME = getenv("SESSION_NAME", "BQGjHhMADUdnk9gOVKSmUg0TQfwSczub4McEHlphlwmOAghSAWdKaTdA5gMTymu5dAY2o8twJ0r8n5J2Lt-7UJhLoasQj6hPwSXFtWQA_rWYlG1yHLPJjCmAYV5ngWdTsTbH3y6mo-YHIddOjnekK7P_kY1tFv1QNzxgCm2aF8X7jS2vbUhntgC3-gaaPxBceiVB9jojfj44EM_cW1VFPJYPJGyzBvHdWC120KVnyOOJI1OEUzQRiwnfwDSl658dAqKSUoacn9OhzJG7EJsLEmsQPnxm9ZyCRv9fYxlObSsoZHt_sD_HQ1Nk_VpfVpLsRWhsR_uO74UDsgxbA_9nA2w5Xh9uXwAAAAFsYo9RAA")

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
