from time import time, sleep
from threading import Thread
import subprocess
import gradio as gr

theme = gr.themes.Soft(
    primary_hue="violet",
    secondary_hue="fuchsia",
    text_size="lg",
    spacing_size="lg",
    radius_size="xxl",
)

class registration:
    registration_process = subprocess.Popen(['./.venv/Scripts/python.exe', './registration.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    logs = ''
    output = gr.Text()
    input = gr.Text()

    def update_logs():
        logs = '| '
        while logs[-1] != ':':
            print(logs)
            logs += registration.registration_process.stdout.read(1).decode()
        registration.logs += logs

    def update_output():
        registration.update_logs()
        return registration.logs
    
    def update_input(text):
        registration.registration_process.stdin.write(text.encode()+b'\n')
        registration.logs = ''
        return ''

def api_start_button_on_click():
    pass

with gr.Blocks(theme=theme) as demo:
    #with gr.Row():
    #    with gr.Group() as api_group:
    #        api_id = gr.Text(label='api_id')
    #        api_hash = gr.Text(label='api_hash')
    #        api_start_button = gr.Button(value='api_start_button')

    #        api_start_button.click(api_start_button_on_click)
    #    with gr.Group() as registration_group:
    #        registration.output = gr.Text(value=registration.update_output, label='registration_output', interactive=False, every=2)
    #        registration.input = gr.Text(label='registration_input')

    #        registration.input.submit(registration.update_input, inputs=[registration.input], outputs=[registration.input])

demo.launch()