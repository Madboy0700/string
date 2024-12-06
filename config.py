from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", 24054192))
API_HASH = getenv("API_HASH", "ed9a8a61a1b4a1ad0915cbe87ba490ed")

BOT_TOKEN = getenv("BOT_TOKEN", "7972411299:AAGK2eJMA0pSWF3l0BqVWppqOrvFS8vjOVI")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://erkbwrs084:909090@cluster0.qdrfgmb.mongodb.net/?retryWrites=true&w=majority")

OWNER_ID = int(getenv("OWNER_ID", 7675940993))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Sohbetikidebir")
