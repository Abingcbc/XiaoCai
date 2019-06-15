import os
import json
import random
import pygame
import time

state = 0
game_map = {}


def drawMap(point_list: list):
    global game_map, state
    if len(point_list) == 1:
        if state == 0:
            game_map = {'point': [point_list[0]]}
            state = 1
        elif state == 1:
            game_map['point'].append(point_list[0])
    else:
        return -1


def saveMapToFile():
    path = './data/music_game_map'
    files = os.listdir(path)
    with open(os.path.join(path, 'map' + str(len(files))), 'w') as f:
        json.dump(game_map, f)
    return len(files)


def readMapFromFile(map_id):
    global game_map
    game_map = json.load('./data/music_game_map/map' + str(map_id))
    return list(game_map.values())


def run():
    while True:
        files = os.listdir('./data/music_game_map')
        global game_map
        game_map = readMapFromFile(random.randint(0,len(files)))
        points = getPointPosition()
        if len(points) == 1:

            # pygame.mixer.init()
            # sound = pygame.mixer.Sound('/Users/cbc/Project/Python/HCI/final_project/data/music_game_map/6856.wav')
            # sound.play()
            # time.sleep(1)
            # pygame.mixer.quit()