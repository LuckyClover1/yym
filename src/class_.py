from fs import *

class module(object):
    def __init__(self,action,templates,match,tryTimes,team_num):
        self.action = action
        self.template = templates
        self.match = match
        self.tryTimes = tryTimes
        self.team_num = team_num

    def click(self):
        point = (0,0)
        matchCount = 0
        while point and point[0] == 0 and point[1] == 0:
            time.sleep(1)
            print('matching ',self.template)
            window_capture(react)
            point = sift_flann_func(self.template)
            if self.match != 'one':
                if self.tryTimes > 0:
                    print('count matchCount ',matchCount)
                    matchCount = matchCount+1
                    if matchCount == self.tryTimes :
                        break
            else:
                move(point)

        if self.match != 'one' and self.match != 'false':
            while point and point[0] > 0 and point[1] > 0:
                move(point)
                time.sleep(0.5)
                print('checking ',self.template)
                window_capture(react)
                point = sift_flann_func(self.template)

    def zudui(self):
        if self.team_num == 2:
            point = (0,0)
            while point and point[0] == 0 and point[1] == 0:
                time.sleep(1)
                print('matching ',self.template)
                window_capture(react)
                point = sift_flann_func(self.template)
        else:
            point = (1,1)
            while point and point[0] > 0 and point[1] > 0:
                time.sleep(1)
                print('matching ',self.template)
                window_capture(react)
                point = sift_flann_func(self.template)


def wait5Sec(clickCount):
    clickCount=clickCount+1
    if(clickCount >= 5):
        print("check fail ,wait 5s.....")
        time.sleep(1)
        print("try check again.")
        return 0
    return clickCount