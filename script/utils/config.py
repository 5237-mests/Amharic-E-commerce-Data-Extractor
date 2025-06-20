import os
from dotenv import load_dotenv

load_dotenv('.env')

TELEGRAM_CONFIG = {
    'api_id': os.getenv('TG_API_ID'),
    'api_hash': os.getenv('TG_API_HASH'),
    'session_name': 'scraping_session'
}