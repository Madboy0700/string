from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", 23915346))
API_HASH = getenv("API_HASH", "3bc48fd6db8e9c1cfdc89c8de742d188")

BOT_TOKEN = getenv("BOT_TOKEN", "7447707289:AAGl9BitaXMeBJBtX-v22gjcj3DfMQQCA2c")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://erkbwrs084:909090@cluster0.qdrfgmb.mongodb.net/?retryWrites=true&w=majority")

OWNER_ID = int(getenv("OWNER_ID", 7305205222))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Sohbetikidebir")
