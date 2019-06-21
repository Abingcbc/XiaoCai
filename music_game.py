import os
import json
import random
import pygame
import time
from point_location import getPointLocation
import cv2
import random
from GestureRecognition import GestureRecognition


class Barrier:
    def __init__(self, ID):
        self.id = ID
        self.length = 0
        self.speed = 0
        self.y = 0

    def init(self):
        self.length = random.randint(1, 10)
        self.speed = random.randint(1,4)
        # barrier's y is the end location of the barrier
        # it increases every time and when it is greater than 9
        # it will be reset to 0
        self.y = -self.length

    def stop(self):
        self.speed = 0
        self.length = 0
        self.y = 0

    def update(self):
        if self.speed > 0:
            self.y += self.speed
            if self.y > 9:
                self.stop()
                return -1
            return 1
        return 0


UNIT = 10
barrier_list = [Barrier(i) for i in range(12)]

def updateBarriers():
    for barrier in barrier_list:
        state = barrier.update()
        if state == 0:
            if random.random() > 0.7:
                barrier.init()

def getNearestBarrier(x, y):
    min_distance = 9999
    for index, barrier in enumerate(barrier_list):
        if barrier.speed > 0:
            if index * UNIT < x < (index+1)*UNIT and y + UNIT * barrier.y > 90:
                return 0
            elif min(abs(x-index*UNIT), abs(y-barrier.y*UNIT)) < min_distance:
                min_distance = min(abs(x-index*UNIT), abs(y-barrier.y*UNIT))
    return min_distance

def playWarningSound(distance):
    if distance <= 0:
        pygame.mixer.init()
        s = pygame.mixer.Sound('data/music_game/music/game_over.wav')
        s.play()
        time.sleep(4)
        pygame.mixer.quit()
        return -1
    elif 0 < distance < 20:
        pygame.mixer.init(frequency=66000)
        s = pygame.mixer.Sound('data/music_game/music/warning.wav')
        s.play()
        time.sleep(1)
        pygame.mixer.quit()
        return 1
    elif 20 <= distance < 40:
        pygame.mixer.init(frequency=44000)
        s = pygame.mixer.Sound('data/music_game/music/warning.wav')
        s.play()
        time.sleep(1)
        pygame.mixer.quit()
        return 2
    elif 40 <= distance < 60:
        pygame.mixer.init(frequency=22000)
        s = pygame.mixer.Sound('data/music_game/music/warning.wav')
        s.play()
        time.sleep(1)
        pygame.mixer.quit()
        return 3
    return 4

gesture_recognition = GestureRecognition()

def run():
    cap = cv2.VideoCapture(0)
    while True:
        points = getPointLocation(cap)
        if gesture_recognition.recognize(points):
            return 1
        updateBarriers()
        min_distance = getNearestBarrier(points[0][0], points[0][1])
        if playWarningSound(min_distance) < 0:
            return -1

