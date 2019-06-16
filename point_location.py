import cv2
import numpy as np

'''
getPointLocation()->获取屏幕上所有激光点质心的坐标，return: list[元素：tuple(x，y)]
main()->测试用，不要调用
'''
#获取激光反射点质心，需输入cap=cv2.VideoCapture(0)
def getPointLocation(cap):

    ret,frame = cap.read()
    frame=cv2.GaussianBlur(frame,(7,7),0)
    frame=cv2.medianBlur(frame,3)
    mask=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    _,mask=cv2.threshold(mask,253,255,cv2.THRESH_BINARY)
    kernal=np.ones((17,17),np.uint8)
    mask=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernal)
    img=cv2.Canny(mask,30,90)
    _,contours,_=cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    mu=list()
    mc=list()
    for contour in contours:
        mu.append(cv2.moments(contour))
    for m in mu:
        if m['m00']!=0:
            mc.append((int(m['m10']/m['m00']),int(m['m01']/m['m00'])))
    return mc,img,mask,frame


def main():
    cap=cv2.VideoCapture(1)
    while True:
        mc,img,mask,frame=getPointLocation(cap)
        for e in mc:
            print(e)
            cv2.circle(frame,e,5,(0,0,255),-1)

        cv2.imshow("img",frame)
        cv2.imshow("mask",mask)
        cv2.imshow("canny",img)
        if cv2.waitKey(1)&0xff == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__=='__main__':
    main()
