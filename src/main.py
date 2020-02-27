from fs import *
from thread_funs import *
import time,_thread

print('start yys')

def start_fight():
    global react
    print('started fight')
    time.sleep(5)
    point = (0,0)
    while point and point[0] == 0 and point[1] == 0:
        time.sleep(1)
        print('waiting ...')
        window_capture(react)
        point = sift_flann_func('resource\\jiangli.bmp')
        # if point and point[0] == 0 and point[1] == 0:
        #     point = sift_flann_func('resource\\shibai.bmp')
        #     if point and point[0] > 0 and point[1] > 0:
        #         print('失败了')

    #给奖励了,或者失败了，返回列表,
    # 老出问题？
    move((int(point[0]+react[0]),int(point[1]+react[1])))
    print('打完了')

    testNum = 0
    for i in range(0,5):
        if(testNum == 2):
            break
        time.sleep(0.5)
        window_capture(react)
        point = sift_flann_func('resource\\jiangli.bmp')
        if point and point[0] != 0 and point[1] != 0:
            move((int(point[0]+react[0]),int(point[1]+react[1])))
        else:
            testNum=testNum + 1
    time.sleep(1)
    window_capture(react)
    point = sift_flann_func('resource\\baiguishoulin.bmp')
    if point and point[0] != 0 and point[1] != 0:
        guiwang()
        # pass
    else:
        print('继续')
        time.sleep(1)
        to_fight()

def guiwang():
    print('打鬼王去喽')
    pass

def to_fight():
    global react
    print('to fight')
    point=(0,0)
    while point and point[0] == 0 and point[1] == 0 :
        time.sleep(1)
        window_capture(react)
        print('matching...')
        point = sift_flann_func('resource\\tiaozhan_yuhun.bmp')
    move((int(point[0]+react[0]),int(point[1]+react[1])))
    start_fight()

react = get_react()
_thread.start_new_thread(start_listener,())
# # for i in range(0,100):
window_capture(react)
to_fight()
