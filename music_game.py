import os
import json
import random
import pygame
import time

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
    elif 0 < temp_distance <

def run():
    while True:
        files = os.listdir('./data/music_game_map')
        game_map = readMapFromFile(random.randint(0,len(files)))
        points = getPointPosition()
        if len(points) == 1:


            # pygame.mixer.init()
            # sound = pygame.mixer.Sound('/Users/cbc/Project/Python/HCI/final_project/data/music_game_map/6856.wav')
            # sound.play()
            # time.sleep(1)
            # pygame.mixer.quit()