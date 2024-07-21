from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", 28736869))
API_HASH = getenv("API_HASH", "258e1a4c3dc48e0c46ee7c8c927ac4a3")

BOT_TOKEN = getenv("BOT_TOKEN", "7489352285:AAEDwxDk-u4os2dzXsUdldjvEASfLw-fwC4")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://mongoguess:guessmongo@cluster0.zcwklzz.mongodb.net/?retryWrites=true&w=majority")

OWNER_ID = int(getenv("OWNER_ID", 6510559004))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/DelularSohbet")
