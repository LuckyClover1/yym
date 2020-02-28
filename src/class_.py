from fs import *

#action :
#    click--匹配点击
#    team--组队
#    once--执行一次
#    try_--尝试执行
class module(object):
    def __init__(self,action,templates,match,tryTimes,team_num):
        self.action = action
        self.template = templates
        self.match = match
        self.tryTimes = tryTimes
        self.team_num = team_num

    def click(self):
        point = (0,0)
        while point and point[0] == 0 and point[1] == 0:
            time.sleep(1)
            print('matching ',self.template)
            window_capture(react)
            point = sift_flann_func(self.template)
        move(point)
        point = sift_flann_func(self.template)
        while point and point[0] > 0 and point[1] > 0:
            move(point)
            time.sleep(0.5)
            print('checking ',self.template)
            window_capture(react)
            point = sift_flann_func(self.template)

    def team(self):
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

    def once(self):
        window_capture(react)
        point = sift_flann_func(self.template)
        count = 0
        while point and point[0] == 0 and point[1] == 0:
            move(point)
            time.sleep(0.5)
            print('matching ',self.template)
            window_capture(react)
            point = sift_flann_func(self.template)
        move(point)


    def try_(self):
        point = sift_flann_func(self.template)
        count = 0
        times = self.tryTimes
        if times or times == 0:
            times = 2
        while count < times:
            move(point)
            time.sleep(0.5)
            print('checking ',self.template)
            window_capture(react)
            point = sift_flann_func(self.template)
            count = count + 1
