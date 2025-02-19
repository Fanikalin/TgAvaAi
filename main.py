from time import time, sleep
import asyncio
from threading import Thread
from qrcode import QRCode
from PIL import Image
import gradio as gr
import os
import shutil

ai_author_name = 'MaxKazak'
ai_model_name = 'ruBert-base-russian-emotion-detection'

if os.path.exists(ai_model_name):
    shutil.rmtree(ai_model_name)

if not os.path.exists('./ai'):
    os.system(f'git clone https://huggingface.co/{ai_author_name}/{ai_model_name}')
    os.rename(f'./{ai_model_name}', 'ai')

import data
import registration
import telegram

os.environ['PYTHONIOENCODING'] =  'utf-8'

theme = gr.themes.Soft(
    primary_hue="violet",
    secondary_hue="fuchsia",
    text_size="lg",
    spacing_size="lg",
    radius_size="xxl",
)

def api_id_submit(api_id):
    data.API.id = int(api_id)

def api_hash_submit(api_hash):
    data.API.hash = api_hash

def api_reload_button_on_click():
    data.save()
    auth_start()
    telegram.init(data.API.id, data.API.hash)

def photo_delete_button_click():
    return  

def photo_add_button_click():
    return

auth_qr = None
auth_status = 'load'

def auth_start():
    global auth_qr, auth_status
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    loop.run_until_complete(registration.qr_auth(auth_image_set))

    auth_status = 'success'

def auth_image_set(url):
    global auth_qr, auth_status
    auth_qr = QRCode()
    auth_qr.add_data(url)
    auth_status = 'process'

def auth_image_get():
    global auth_qr, auth_status
    if auth_status == 'process':
        return auth_qr.make_image().get_image()
    elif auth_status == 'load':
        return Image.open('./data/loading.png')
    elif auth_status == 'success':
        return Image.open('./data/success.png')

with gr.Blocks(theme=theme) as demo:
    with gr.Row():
        with gr.Column():
            with gr.Group() as api_group:
                api_id = gr.Text(value=data.API.id, label='api_id')
                api_hash = gr.Text(value=data.API.hash, label='api_hash')
                api_reload_button = gr.Button(value='api_reload_button')

                api_id.submit(api_id_submit, inputs=[api_id])
                api_hash.submit(api_hash_submit, inputs=[api_hash])
                api_id.blur(api_id_submit, inputs=[api_id])
                api_hash.blur(api_hash_submit, inputs=[api_hash])
                api_reload_button.click(api_reload_button_on_click)
        with gr.Column():
            with gr.Group() as auth_group:

                auth_image = gr.Image(auth_image_get, interactive=False, every=1, width='300px')

demo.launch()