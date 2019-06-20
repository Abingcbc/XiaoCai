from point_location import getPointLocation
from GestureRecognition import GestureRecognition
from ai import playAIMusic
import pygame.mixer as pmx
import pygame
import cv2
import numpy as np
import _thread
import threading

class AIThread (threading.Thread):
    def __init__(self, threadID, name, mlist):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.mlist = mlist
    def run(self):
        playAIMusic(self.mlist)



pygame.init()

def playMusic():
    now_status_x=1
    now_status_y=1
    last_status_x=0
    last_status_y=0
    cap=cv2.VideoCapture(1)
    recognition=GestureRecognition()
    history=list()
    mat=np.array([[17,21,23,24],[32,44,46,51],[52,53,54,55],[56,66,73,75]])
    while True:
        mc,frame,mask=getPointLocation(cap)
        width=int(frame.shape[0])
        length=int(frame.shape[1])

        if recognition.recognize(mc):
            break
        if len(mc)==0:
            last_status_y=0
            last_status_x=0
        if len(mc)>=1:
            point=mc[0]
            now_status_x=int(point[0]*4/length)
            now_status_y=int(point[1]*4/width)

            if now_status_x!=last_status_x or now_status_y!=last_status_y:
                meme=pmx.Sound('data/music/'+str(mat[now_status_x,now_status_y])+'.wav')
                meme.play()
                history.append(mat[now_status_x,now_status_y])
            last_status_x=now_status_x
            last_status_y=now_status_y
        for e in mc:
            cv2.circle(frame,e,2,(0,0,255),-1)


        cv2.line(frame,(int(length/4),0),(int(length/4),int(width)),(255,0,0),1)
        cv2.line(frame,(int(2*length/4),0),(int(2*length/4),int(width)),(255,0,0),1)
        cv2.line(frame,(int(3*length/4),0),(int(3*length/4),int(width)),(255,0,0),1)
        cv2.line(frame,(0,int(width/4)),(length,int(width/4)),(255,0,0),1)
        cv2.line(frame,(0,int(2*width/4)),(length,int(2*width/4)),(255,0,0),1)
        cv2.line(frame,(0,int(3*width/4)),(length,int(3*width/4)),(255,0,0),1)
        cv2.imshow("img",frame)
        cv2.imshow("mask",mask)

        if cv2.waitKey(1)==ord('q'):
            break
    file=open('resource/music.txt','w')
    file.truncate()
    for m in history:
        file.write(str(m)+' ')
    cv2.destroyAllWindows()

def playMusicWithAI():
    now_status_x=1
    now_status_y=1
    last_status_x=0
    last_status_y=0
    cap=cv2.VideoCapture(1)
    recognition=GestureRecognition()
    mat=np.array([[17,21,23,24],[32,44,46,51],[52,53,54,55],[56,66,73,75]])
    history=list()
    musicList=list() 
    maxlen=5
    while True:
        mc,frame,mask=getPointLocation(cap)
        width=int(frame.shape[0])
        length=int(frame.shape[1])

        if recognition.recognize(mc):
            break
        if len(mc)==0:
            last_status_y=0
            last_status_x=0
        if len(mc)>=1:
            point=mc[0]
            now_status_x=int(point[0]*4/length)
            now_status_y=int(point[1]*4/width)
            if now_status_x!=last_status_x or now_status_y!=last_status_y:
                meme=pmx.Sound('data/music/'+str(mat[now_status_x,now_status_y])+'.wav')
                meme.play()
                musicList.append(mat[now_status_x,now_status_y])
                history.append(mat[now_status_x,now_status_y])
                if len(musicList)>=maxlen:
                    thread=AIThread(1,'a',musicList)
                    thread.start()
                    musicList.clear()

            last_status_x=now_status_x
            last_status_y=now_status_y
        for e in mc:
            cv2.circle(frame,e,2,(0,0,255),-1)


        cv2.line(frame,(int(length/4),0),(int(length/4),int(width)),(255,0,0),1)
        cv2.line(frame,(int(2*length/4),0),(int(2*length/4),int(width)),(255,0,0),1)
        cv2.line(frame,(int(3*length/4),0),(int(3*length/4),int(width)),(255,0,0),1)
        cv2.line(frame,(0,int(width/4)),(length,int(width/4)),(255,0,0),1)
        cv2.line(frame,(0,int(2*width/4)),(length,int(2*width/4)),(255,0,0),1)
        cv2.line(frame,(0,int(3*width/4)),(length,int(3*width/4)),(255,0,0),1)
        cv2.imshow("img",frame)
        cv2.imshow("mask",mask)

        cv2.waitKey(1)
    file=open('resource/music.txt','w')
    file.truncate()
    for m in history:
        file.write(str(m)+' ')

    cv2.destroyAllWindows()
        
def main():
    playMusic()


main()




