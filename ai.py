import pygame
import os


def playAIMusic(input_list: list):
    pygame.mixer.init()
    generateAIMusic(input_list)
    for file in os.listdir('./generated'):
        file_path = os.path.join('./generated',file)
        pygame.mixer.music.load(file_path)
        clock = pygame.time.Clock()
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            clock.tick(30)


def generateAIMusic(input_list: list):
    os.system('pianoroll_rnn_nade_generate \
                --bundle_file=/Users/cbc/Project/Python/HCI/final_project/pianoroll_rnn_nade.mag \
                --output_dir=./generated \
                --num_outputs=10 \
                --num_steps=128 \
                --primer_pitches=' + str(input_list))
