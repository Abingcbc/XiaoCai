import os
import json
import random
import pygame
import time
from point_location import getPointLocation
import cv2

state = 0
game_map_to_save = {}


def drawMap(point_list: list):
    global game_map_to_save, state
    if len(point_list) == 1:
        if state == 0:
            game_map_to_save  = {'point': [point_list[0]]}
            state = 1
        elif state == 1:
            game_map_to_save ['point'].append(point_list[0])
    else:
        return -1


def saveMapToFile():
    if len(game_map_to_save) == 0:
        return -1
    path = './data/music_game_map'
    files = os.listdir(path)
    with open(os.path.join(path, 'map' + str(len(files))), 'w') as f:
        json.dump(game_map_to_save, f)
    return len(files)


def readMapFromFile(map_id):
    game_map = json.load('./data/music_game_map/map' + str(map_id))
    return list(game_map.values())

def getNearestBarrier(point, game_map):
    temp_index = -1
    temp_distance = 999999
    for i, p in enumerate(game_map):
        if abs(point[0]-p[0]) + abs(point[1]-p[1]) < temp_distance:
            temp_index = i
            temp_distance = abs(point[0]-p[0]) + abs(point[1]-p[1])
    if temp_distance == 0:
        return -1
    elif 0 < temp_distance < 50:
        pygame.mixer.init(frequency=66000)
        s = pygame.mixer.Sound()
        s.play()
        time.sleep(1)
        pygame.mixer.quit()
        return 1
    elif 50 <= temp_distance < 100:
        pygame.mixer.init(frequency=44000)
        s = pygame.mixer.Sound()
        s.play()
        time.sleep(1)
        pygame.mixer.quit()
        return 2
    elif 100 <= temp_distance < 150:
        pygame.mixer.init(frequency=22000)
        s = pygame.mixer.Sound()
        s.play()
        time.sleep(1)
        pygame.mixer.quit()
        return 3
    elif 150 <= temp_distance < 200:
        pygame.mixer.init(frequency=11000)
        s = pygame.mixer.Sound()
        s.play()
        time.sleep(1)
        pygame.mixer.quit()
        return 4



def run():
    cap = cv2.VideoCapture(0)
    while True:
        files = os.listdir('./data/music_game_map')
        game_map = readMapFromFile(random.randint(0,len(files)))
        points = getPointLocation(cap)
        if len(points) == 1:
            result = getNearestBarrier(points[0], game_map)
            if result == -1:
                #TODO: game lose music
                break
        else:


