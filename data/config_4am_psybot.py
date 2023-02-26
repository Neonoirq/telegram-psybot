import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

BOT_TOKEN = str(os.getenv('BOT_TOKEN'))

EMAIL_TOKEN = str(os.getenv('EMAIL_TOKEN'))

EMAIL_NAME = str(os.getenv('EMAIL_NAME'))