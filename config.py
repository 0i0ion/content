import os
import logging
from operator import add
from logging.handlers import RotatingFileHandler

REQUEST1 = os.environ.get("REQUEST1", "https://t.me/+7nH3rPTjXdNkYzc1")
REQUEST2 = os.environ.get("REQUEST2", "https://t.me/+NbwZkqpkctRmZTZl")

TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6737569405:AAHwpHE4G_DTwP0vmFYdS1j9pU8DgOpF2ao") #@Hentai
APP_ID = int(os.environ.get("APP_ID", "25695562"))
API_HASH = os.environ.get("API_HASH", "0b691c3e86603a7e34aae0b5927d725a")
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001929558021"))
OWNER_ID = int(os.environ.get("OWNER_ID", "1895952308"))

PORT = os.environ.get("PORT", "8080")
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://skiliggeeXporter:skiliggeeXporter@cluster0.tdxtakc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "AdultElixir")

SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "runurl.in")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "3a2c084d61d0813b05a00cd9ba564e92e39f92cb")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', "86400")) # Add time in seconds
TUT_VID = os.environ.get("TUT_VID","https://t.me/Anime_Elixir/8")
IS_VERIFY = os.environ.get("IS_VERIFY","True")

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "400"))
START_MSG = os.environ.get("START_MESSAGE", "<blockquote><b>ℹ️ Hello {mention} Welcome to our 18+ Contact Provider Bot. Exclusively work for <a href='https://t.me/Adult_Elixir'>Elixir of Lust</a></b></blockquote>")
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<blockquote><b>ℹ️ Hello {mention}\nYou need to join in my Channel to use me\nKindly Please join Channel</b></blockquote>")

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1895952308").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER_ID)
ADMINS.append(6878668907)

CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", "True")

BOT_STATS_TEXT = "<b>BOT UPTIME {uptime}</b>"
USER_REPLY_TEXT = "<blockquote><b>🔴 Don't send me messages directly I'm only File Share bot!</b></blockquote>"

LOG_FILE_NAME = "filesharingbot.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
