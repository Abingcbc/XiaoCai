import os
import json
import random
import pygame
import time
from point_location import getPointLocation
import cv2
import random


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
barrier_signal_list = [False]*12
barrier_list = [Barrier(i) for i in range(10)]

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
            if min(abs(x-index*10), abs(y-barrier.y*10)):
                min_distance = min(abs(x-index*10), abs(y-barrier.y*10))
    return min_distance

def playWarningSound(distance):
    

def run():
    cap = cv2.VideoCapture(0)
    while True:
        points = getPointLocation(cap)



