from img import *
from ui import *
import time


class Module(object):
    def __init__(self, action, templates, team_num):
        self.action = action
        self.template = templates
        self.team_num = team_num
        
        
    def click_once(self):
        point = (0, 0)
        while point and point[0] == 0 and point[1] == 0:
            time.sleep(0.5)
            print('matching ', self.template)
            window_capture()
            point = match_template(self.template)
        move_click(point)
        

    def click(self):
        point = (0, 0)
        max_try = 1000
        while point and max_try > 0 and point[0] == 0 and point[1] == 0:
            time.sleep(1)
            print('matching ', self.template)
            window_capture()
            point = match_template(self.template)
            max_try = max_try - 1
        move_click(point)
        point = match_template(self.template)
        while point and point[0] > 0 and point[1] > 0:
            move_click(point)
            time.sleep(1)
            print('checking ', self.template)
            window_capture()
            point = match_template(self.template)

    def team(self):
        if self.team_num == 2:
            point = (0, 0)
            while point and point[0] == 0 and point[1] == 0:
                time.sleep(0.5)
                print('matching ', self.template, point)
                window_capture()
                point = match_template(self.template)
        else:
            point = (1, 1)
            while point and point[0] > 0 and point[1] > 0:
                time.sleep(0.5)
                print('matching ', self.template, point)
                window_capture()
                point = match_template(self.template)


