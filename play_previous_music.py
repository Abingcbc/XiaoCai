import pygame
import time

def run():
    with open('resource/music.txt') as file:
        s = file.readline()
    sound_list = s.split(' ')
    pygame.mixer.init()
    for beat in sound_list:
        s = pygame.mixer.Sound('data/music/'+beat+'.wav')
        s.play()
        time.sleep(1)