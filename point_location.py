import cv2
import numpy as np


def getPointLocation(cap):

    ret,frame = cap.read()
    frame=cv2.resize(frame,(120,90))
    #frame=cv2.GaussianBlur(frame,(3,3),0)
    #frame=cv2.medianBlur(frame,3)
    mask=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    _,mask=cv2.threshold(mask,250,255,cv2.THRESH_BINARY)
    kernal=np.ones((4,4),np.uint8)
    mask=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernal)
    #img=cv2.Canny(mask,30,90)
    _,contours,_=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    mu=list()
    mc=list()
    for contour in contours:
        mu.append(cv2.moments(contour))
    for m in mu:
        if m['m00']!=0:
            mc.append((int(m['m10']/m['m00']),int(m['m01']/m['m00'])))
    return mc,frame,mask


def main():
    cap=cv2.VideoCapture(1)

    while True:
        mc,frame,mask=getPointLocation(cap)
        for e in mc:
            cv2.circle(frame,e,5,(0,0,255),-1)


        length=int(frame.shape[1])
        width=int(frame.shape[0])
        cv2.line(frame,(int(length/4),0),(int(length/4),int(width)),(255,0,0),3)
        cv2.line(frame,(int(2*length/4),0),(int(2*length/4),int(width)),(255,0,0),3)
        cv2.line(frame,(int(3*length/4),0),(int(3*length/4),int(width)),(255,0,0),3)
        cv2.line(frame,(0,int(width/4)),(length,int(width/4)),(255,0,0),3)
        cv2.line(frame,(0,int(2*width/4)),(length,int(2*width/4)),(255,0,0),3)
        cv2.line(frame,(0,int(3*width/4)),(length,int(3*width/4)),(255,0,0),3)
        cv2.imshow("img",frame)
        cv2.imshow("mask",mask)

        if cv2.waitKey(1)&0xff == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__=='__main__':
    main()
