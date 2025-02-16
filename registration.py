from telethon import TelegramClient

import data

api_id = data.API.id
api_hash = data.API.hash

client = TelegramClient('./data/telegram', api_id, api_hash, system_version='4.16.30-vxCUSTOM')

client.start()

#from time import time, sleep
#
#while True:
#    print(time())

print('success')