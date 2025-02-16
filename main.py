from telethon import TelegramClient, events
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
import text_emo
from time import time, sleep
from pprint import pprint
import os


api_id = 0
api_hash = ''

client = TelegramClient('', api_id, api_hash,
                        system_version='4.16.30-vxCUSTOM')

import asyncio

async def main():
    while True:
        await client.start()
        await asyncio.sleep(3600)
        await client.disconnect()

client.loop.run_until_complete(main())