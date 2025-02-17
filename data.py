import base64

class API:
    __file = str()
    id = int()
    hash = str()

    def load():
        API.__file = base64.b64decode(open('./data/API', 'rb').read()).decode().split('\n')
        API.id = int(API.__file[0])
        API.hash = API.__file[1]

    def save():
        API.__file = open('./data/API', 'wb')
        API.__file.write(
            base64.encode(
                f'{API.id}\n{API.hash}'.encode()
            )
        )

def load():
    API.load()

def save():
    API.save()

API.load()