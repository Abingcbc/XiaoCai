import time

class gestureRecognition:
    def __init__(self):
        self.now=0
        self.past=0
        self.times=False
        self.old_mc=list()


    def recognize(self,mc):
        flag=False
        if self.times:
            self.now=time.clock()
        if len(mc)>2:
            if self.times and self.now-self.past>0.2:
                 if mc[0][1]<self.old_mc[0][1] and mc[1][1]<self.old_mc[1][1]:
                    if self.old_mc[0][1]-mc[0][1]>=20:
                        flag=True
                 self.times=False
            elif not self.times:
                self.past=time.clock()
                self.old_mc=mc
                self.times=True
        return flag
