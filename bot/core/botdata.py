# File containing global variables for bot.

from dotenv import load_dotenv
from os import environ, path
import logging

logger = logging.getLogger(__name__)

load_dotenv()

try:
    token: str = environ["TOKEN"]
except KeyError:
    logger.critical("No token found in .env file, exiting")
    exit(1)

parent: str = f"{path.dirname(path.realpath(__file__))}/.."

bot_id: int = 0
bot_avatar_url: str = ""
date_format: str = "%Y/%m/%d %H:%M:%S"
