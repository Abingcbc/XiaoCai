import pygame
import os
import requests
import datetime
from io import BytesIO

# This function should run in a new thread
def playAIMusic(input_list: list):
    # Assume that mixer has been inited
    input_list = [str(x) for x in input_list]
    for i in os.listdir('generated'):
        path_file = os.path.join('generated',i)
        if os.path.isfile(path_file):
            os.remove(path_file)
    sendRequest(input_list)
    for file in os.listdir('generated'):
        file_path = os.path.join('generated',file)
        print(file_path)
        pygame.mixer.music.load(file_path)
        clock = pygame.time.Clock()
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            clock.tick(30)


def generateAIMusic(input_list: list):
    # remove all previous files
    for i in os.listdir('/root/Desktop/Xiaocai/static'):
        path_file = os.path.join('/root/Desktop/Xiaocai/static',i)
        if os.path.isfile(path_file):
            os.remove(path_file)
    os.system('pianoroll_rnn_nade_generate \
                --bundle_file=/root/Desktop/Xiaocai/pianoroll_rnn_nade.mag \
                --output_dir=/root/Desktop/Xiaocai/static \
                --num_outputs=1 \
                --num_steps=128 \
                --primer_pitches=' + '"'+str(input_list)+'"')

def sendRequest(input_list: list):
    beats_string = '_'.join(input_list)
    r = requests.get('http://47.103.21.70/ai/'+beats_string)
    file_name = str(datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d-%X'))
    with open('./generated/'+file_name+'.mid', 'wb') as code:
        code.write(r.content)
        print('--- Download Success ---')

