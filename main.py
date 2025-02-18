from time import time, sleep
from threading import Thread
from telethon import TelegramClient
import gradio as gr
import os

ai_author_name = 'MaxKazak'
ai_model_name = 'ruBert-base-russian-emotion-detection'

if not os.path.exists('./ai'):
    os.system(f'git clone https://huggingface.co/{ai_author_name}/{ai_model_name}')
    os.rename(f'./{ai_model_name}', 'ai')

import data
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
    telegram.init(data.API.id, data.API.hash)

with gr.Blocks(theme=theme) as demo:
    with gr.Row():
        with gr.Group() as api_group:
            api_id = gr.Text(value=data.API.id, label='api_id')
            api_hash = gr.Text(value=data.API.hash, label='api_hash')
            api_reload_button = gr.Button(value='api_reload_button')

            api_id.submit(api_id_submit, inputs=[api_id])
            api_hash.submit(api_hash_submit, inputs=[api_hash])
            api_reload_button.click(api_reload_button_on_click)

demo.launch()