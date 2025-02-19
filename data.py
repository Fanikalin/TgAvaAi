import base64
import os

class API:
    __file = str()
    id = int()
    hash = str()

    def load():
        try:
            API.__file = base64.b64decode(open('./data/API', 'rb').read()).decode().split('\n')
            API.id = int(API.__file[0])
            API.hash = API.__file[1]
        except ValueError:
            API.id = None
            API.hash = None

    def save():
        API.__file = open('./data/API', 'wb')
        API.__file.write(
            base64.b64encode(
                f'{API.id}\n{API.hash}'.encode()
            )
        )

class AVATARS:
    emotions = os.listdir('./data/avatars')
    avatars = {emo:[p for p in os.listdir(f'./data/avatars/{emo}')] for emo in emotions}

def load():
    API.load()

def save():
    API.save()

API.load()