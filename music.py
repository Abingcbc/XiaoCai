from point_location import getPointLocation
import cv2

def playMusic():
    now_status_x=0
    now_status_y=0
    last_status_x=0
    last_status_y=0
    cap=cv2.VideoCapture(1)
    while True:
        mc,frame,_,_=getPointLocation(cap)
        width=int(frame.shape[0])
        length=int(frame.shape[1])
        if len(mc)==1:
            point=mc[0]
            #判断x轴区域
            if point[0]<=length/4:
                now_status_x=1
            elif point[0]<=length/2:
                now_status_x=2
            elif point[0]<=3*length/4:
                now_status_x=3
            elif point[0]<=length:
                now_status_x=4
            #判断y轴区域
            if point[1]<=width/4:
                now_status_y=1
            elif point[1]<=width/2:
                now_status_y=2
            elif point[1]<=3*width/4:
                now_status_y=3
            elif point[1]<=width:
                now_status_y=4
            if now_status_x!=last_status_x or now_status_y!=last_status_y:
                
            last_status_x=now_status_x
            last_status_y=now_status_y
        for e in mc:
            cv2.circle(frame,e,5,(0,0,255),-1)
        cv2.line(frame,(int(length/4),0),(int(length/4),int(width)),(255,0,0),3)
        cv2.line(frame,(int(2*length/4),0),(int(2*length/4),int(width)),(255,0,0),3)
        cv2.line(frame,(int(3*length/4),0),(int(3*length/4),int(width)),(255,0,0),3)
        cv2.line(frame,(0,int(width/4)),(length,int(width/4)),(255,0,0),3)
        cv2.line(frame,(0,int(2*width/4)),(length,int(2*width/4)),(255,0,0),3)
        cv2.line(frame,(0,int(3*width/4)),(length,int(3*width/4)),(255,0,0),3)
        cv2.imshow("frame",frame)
        cv2.waitKey(1)
    cv2.destroyAllWindows()

def main():
    playMusic()



main()



