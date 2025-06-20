import asyncio
from telethon import TelegramClient
import csv
import os
from typing import List, Optional

class TelegramScraper:
    def __init__(self, session_name: str, api_id: int, api_hash: str):
        self.client = TelegramClient(session_name, api_id, api_hash)
        self.media_dir = '../data/telegram_media'
        os.makedirs(self.media_dir, exist_ok=True)

    async def _scrape_channel(self, channel_username: str, writer: csv.writer):
        """Internal method to scrape a single channel"""
        try:
            entity = await self.client.get_entity(channel_username)
            channel_title = entity.title
            print(f"Scraping {channel_title} (@{channel_username})...")
            
            async for message in self.client.iter_messages(entity, limit=1000):
                await asyncio.sleep(0.05)  # Rate limiting
                
                media_path = None
                if message.media and hasattr(message.media, 'photo'):
                    filename = f"{channel_username}_{message.id}.jpg"
                    media_path = os.path.join(self.media_dir, filename)
                    await self.client.download_media(message.media, file=media_path)
                
                writer.writerow([
                    channel_title,
                    channel_username,
                    message.id,
                    message.text,
                    message.date,
                    media_path
                ])
        except Exception as e:
            print(f"⚠️ Error in {channel_username}: {e}")

    async def scrape_channels(self, channels: List[str], output_csv: str = 'telegram_data.csv'):
        """Main scraping method for multiple channels"""
        with open(output_csv, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Channel', 'Username', 'Message ID', 'Text', 'Date', 'Media Path'])
            
            for channel in channels:
                await self._scrape_channel(channel, writer)
    
    async def run(self, channels: List[str]):
        """Start the scraping process"""
        await self.client.start()
        await self.scrape_channels(channels)
        await self.client.disconnect()
