import os
from pathlib import Path

from dotenv import load_dotenv
from motor import motor_asyncio

# Base project settings
BASE_DIR = Path(__file__).parent.parent

DOTENV_PATH = ".env"
load_dotenv(dotenv_path=os.path.join(BASE_DIR, DOTENV_PATH))


APP_NAME = "Mykolaiv city bot Backend"
APP_VERSION = "0.0.1beta"


MONGO_URL = os.getenv("MONGO_DB")
DB_NAME = os.getenv("DB_NAME")

client = motor_asyncio.AsyncIOMotorClient(MONGO_URL)

database = client[DB_NAME]
