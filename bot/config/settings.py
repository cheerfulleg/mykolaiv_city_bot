import logging
import os
from pathlib import Path
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

BASE_DIR = Path(__file__).parent.parent

DOTENV_PATH = ".env"
load_dotenv(dotenv_path=os.path.join(BASE_DIR, DOTENV_PATH))

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

API_TOKEN = os.getenv("API_TOKEN")
DOMAIN = os.getenv("DOMAIN")

bot = Bot(token=API_TOKEN)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


