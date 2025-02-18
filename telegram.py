import asyncio
import random
import os
from telethon import TelegramClient, events, functions

from emotions import Analyzer

profile_photo_emo_now = None
async def update_profile_photo(client: TelegramClient, analyzer: Analyzer):
    global profile_photo_emo_now
    
    profile_photo_emo_new = analyzer.pull()

    if profile_photo_emo_new != profile_photo_emo_now:
        if profile_photo_emo_now != None:
            await client(functions.photos.DeletePhotosRequest(id=[(await client.get_profile_photos('me'))[0]]))

        profile_photo_file = os.path.join(f'./data/avatars/{profile_photo_emo_new}', random.choice(os.listdir(f'./data/avatars/{profile_photo_emo_new}')))
        if profile_photo_file.endswith(('.mp4', '.gif')):
            await client(functions.photos.UploadProfilePhotoRequest(video=await client.upload_file(profile_photo_file)))
        else:
            await client(functions.photos.UploadProfilePhotoRequest(file=await client.upload_file(profile_photo_file)))

    profile_photo_emo_now = profile_photo_emo_new

def init(api_id, api_hash):

    asyncio.set_event_loop(asyncio.new_event_loop())

    analyzer = Analyzer()
    client = TelegramClient('./data/telegram', api_id, api_hash, system_version='4.16.30-vxCUSTOM')
    client.start()

    @client.on(events.NewMessage(from_users=['@fanikalin']))
    async def NewMessage_handler(event: events.NewMessage.Event):
        text = event.message.message
        
        analyzer.push(text)

        await update_profile_photo(client, analyzer)
        
    client.run_until_disconnected()