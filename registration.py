import data

from telethon import TelegramClient, errors


async def qr_auth(display_func):
    client = TelegramClient('./data/telegram', data.API.id, data.API.hash, system_version='4.16.30-vxCUSTOM')

    await client.connect()

    if await client.is_user_authorized():
        return client.disconnect()

    qr_login = await client.qr_login()

    res = False
    while not res:
        display_func(qr_login.url)
        
        try:
            res = await qr_login.wait(10)
        except errors.SessionPasswordNeededError:
            res = False
            while not res:
                try:
                    res = True
                    await client.sign_in(password=input('Telegram password: '))
                except errors.PasswordHashInvalidError:
                    res = False
                    print('error')
        except:
            await qr_login.recreate()

    return client.disconnect()