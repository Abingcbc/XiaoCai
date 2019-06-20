# _*_ coding:UTF-8 _*_

import snowboydecoder
import threading
import pygame
import time
from music import playMusic
import music_game
import play_previous_music
from music import playMusicWithAI

# import model
model_xctx = 'xiaocaitongxue.pmdl'
model_func = ['alexa.umdl', 'Hey Friday.pmdl', 'Jarvis.pmdl', 'snowboy.umdl']


# interrupted variable
interrupted_xctx = False
interrupted_func = False


# create thread

def interrupt_callback_xctx():
    global interrupted_xctx
    return interrupted_xctx

def time() :
    global interrupted_func
    global thread_time

    interrupted_func = False
    tick_0 = time.time()
    tick_1 = time.time()
    while(tick_1-tick_0<5):
        tick_1 = time.time()
    interrupted_func = True
    print('Over!')

def interrupt_callback_xctx():
    global interrupted_xctx
    return interrupted_xctx
def interrupt_callback_func():
    global interrupted_func
    return interrupted_func

def wake_up():
    global detector_xctx

    #set model and sensitivity
    detector_xctx = snowboydecoder.HotwordDetector(model_xctx, sensitivity=0.8)
    print('Listening(xctx)...')
    detector_xctx.start(detected_callback=callback_xctx,
                        interrupt_check=interrupt_callback_xctx,
                        sleep_time=0.03)

def callback_piano():
    print("\npiano\n")
    global detector_func
    detector_func.terminate()

    pygame.mixer.init()
    track = pygame.mixer.music.load('X_piano.mp3')
    pygame.mixer.music.play()
    time.sleep(1)
    pygame.mixer.quit()

    playMusic()

    wake_up()

def callback_game():
    print("\ngame\n")
    global detector_func
    detector_func.terminate()

    pygame.mixer.init()
    track = pygame.mixer.music.load('X_game.mp3')
    pygame.mixer.music.play()
    time.sleep(2)
    pygame.mixer.quit()

    music_game.run()

    wake_up()

def callback_music():
    print("\nmusic\n")
    global detector_func
    detector_func.terminate()

    pygame.mixer.init()
    track = pygame.mixer.music.load('X_music')
    pygame.mixer.music.play()
    time.sleep(1)
    pygame.mixer.quit()

    play_previous_music.run()

    wake_up()

def callback_ai():
    print("\nai\n")
    global detector_func
    detector_func.terminate()

    pygame.mixer.init()
    track = pygame.mixer.music.load('X_ai.mp3')
    pygame.mixer.music.play()
    time.sleep(1)
    pygame.mixer.quit()

    playMusicWithAI()


    wake_up()

def callback_xctx():
    print('You said xctx!')
    global detector_xctx
    detector_xctx.terminate()

    pygame.mixer.init()
    track = pygame.mixer.music.load('Xctx.mp3')
    pygame.mixer.music.play()
    time.sleep(9)
    pygame.mixer.quit()

    global detector_func
    detector_func = snowboydecoder.HotwordDetector(model_func,
                                                   sensitivity=[0.6, 0.7, 0.5, 0.5])
    callbacks = [lambda:callback_piano(),
                 lambda:callback_game(),
                 lambda:callback_music(),
                 lambda:callback_ai()]
    print("Listening(func)...")
    detector_func.start(detected_callback=callbacks,
                        interrupt_check=interrupt_callback_func,
                        sleep_time=0.03)
    print("end")


if __name__ == '__main__':
    wake_up()
