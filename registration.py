import data

from telethon import TelegramClient

client = TelegramClient('./data/telegram', data.API.id, data.API.hash, system_version='4.16.30-vxCUSTOM')

client.start()

print('-=-=success-=-=')