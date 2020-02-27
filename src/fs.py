import cv2
import random
import os,time
import win32gui, win32ui, win32con, win32api

local = os.path.abspath(os.path.dirname(__file__))
def get_randxy(x, y):
    """产生一个在x,y二维区域内的随机位置,x,y为两个元素的列表，变量范围"""
    xc = random.randint(x[0], y[0])
    yc = random.randint(x[1], y[1])

    return xc,yc

def get_react():
    rate = 1
    #获取后台窗口的句柄，注意后台窗口不能最小化
    hWnd = win32gui.FindWindow(None,'阴阳师-网易游戏') #窗口的类名可以用Visual Studio的SPY++工具获取
    #获取句柄窗口的大小信息
    left, top, right, bot = win32gui.GetWindowRect(hWnd)
    top = (int)(top * rate)
    left = (int)(left * rate)
    right = (int)(right * rate)
    bot = (int)(bot * rate)
    return (left,top,right,bot)

#截图
react = get_react()
def refreshScance():
    global react
    window_capture(react)
    time.sleep(0.5)

def refreshReact():
    global react
    react = get_react()
    time.sleep(10)

def wait(t):
    react = get_react()
    for i in (0,t*5):
        x,y = get_randxy((react[0],react[1]),(react[2],react[3]))
        move((x,y))
        time.sleep(0.2)

def window_capture(react):
    react = get_react()
    left = react[0]
    top = react[1]
    right = react[2]
    bot = react[3]
    width = right - left
    height = bot - top

    #返回句柄窗口的设备环境，覆盖整个窗口，包括非客户区，标题栏，菜单，边框
    hWndDC = win32gui.GetWindowDC(0)
    #创建设备描述表
    mfcDC = win32ui.CreateDCFromHandle(hWndDC)
    #创建内存设备描述表
    saveDC = mfcDC.CreateCompatibleDC()
    #创建位图对象准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    #为bitmap开辟存储空间
    saveBitMap.CreateCompatibleBitmap(mfcDC,width,height)
    #将截图保存到saveBitMap中
    saveDC.SelectObject(saveBitMap)
    #保存bitmap到内存设备描述表
    saveDC.BitBlt((0,0), (width,height), mfcDC, (left, top), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, local + '\\test\\test.bmp')

def sift_flann_func(template):
    test = 'test\\test.bmp'
    img1 = cv2.imread(local+'\\'+ template,0) # queryImage
    img2 = cv2.imread(local+'\\' + test,0) # trainImage

    sift = cv2.xfeatures2d.SIFT_create()
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)

    #指定算法
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks = 50) #指定递归次数

    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des1, des2, k=2)

    match_points = []
    for i,(m,n) in enumerate(matches):
        #丢弃错误匹配，这里的0.7不知道是啥，反正效果挺好
        if m.distance < 0.7 * n.distance:
            #匹配点位置
            x = kp2[m.trainIdx].pt[0]
            y = kp2[m.trainIdx].pt[1]
            # break;
            match_points.append((x,y))
    if len(match_points)<10:
        return (0,0)
    match_points.sort()
    width = img1.shape[1]
    height = img1.shape[0]
    x_0 = 0
    y_0 = 0
    p_count = 1
    for i,p in enumerate(match_points):
        if i == 0:
            x_0 = p[0]
            y_0 = p[1]
        elif abs(match_points[i-1][0] - p[0]) < width \
                and abs(match_points[i-1][1] - p[1]) < height:
            x_0 = x_0 + p[0]
            y_0 = y_0 + p[1]
            p_count = p_count+1
    matchX = int(x_0/p_count)
    matchY = int(y_0/p_count)
    return (matchX,matchY)

def avg_point(tmp):
    if len(tmp>0):
        xx = 0
        yy = 0
        for x,y in tmp:
            xx=xx+x
            yy=yy+y
        return (xx / len(tmp),yy/len(tmp))
    return (0,0)

def move(point):
    win32api.SetCursorPos(point)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
