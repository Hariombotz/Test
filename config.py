import os
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ADMIN_ID = int(os.getenv("ADMIN_ID"))
LOG_CHANNEL = os.getenv("LOG_CHANNEL")
MONGO_URI = os.getenv("MONGO_URI")
