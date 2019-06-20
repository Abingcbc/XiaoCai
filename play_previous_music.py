import pygame
import time
import cv2
from GestureRecognition import GestureRecognition
from point_location import getPointLocation

def run():
    with open('resource/music.txt') as file:
        s = file.readline().strip()
    sound_list = s.split(' ')
    pygame.mixer.init()
    gensture_recognition = GestureRecognition()
    cap = cv2.VideoCapture(1)
    for beat in sound_list:
        s = pygame.mixer.Sound('data/music/'+beat+'.wav')
        s.play()
        time.sleep(1)
        points,frame,mask = getPointLocation(cap)

        if gensture_recognition.recognize(points):
            return -1

    return 1

run()
