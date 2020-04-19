import win32api
import win32con
import win32gui
import win32ui

import global_


def get_react():
    rate = 1
    # 获取后台窗口的句柄，注意后台窗口不能最小化
    hWnd = win32gui.FindWindow(None, '阴阳师-网易游戏')  # 窗口的类名可以用Visual Studio的SPY++工具获取
    # 获取句柄窗口的大小信息
    left, top, right, bot = win32gui.GetWindowRect(hWnd)
    top = int(top * rate)
    left = int(left * rate) + 7
    right = int(right * rate)
    bot = int(bot * rate)
    return left, top, right, bot


def window_capture():
    react = get_react()
    left = react[0]
    top = react[1]
    right = react[2]
    bot = react[3]
    width = right - left
    height = bot - top

    # 返回句柄窗口的设备环境，覆盖整个窗口，包括非客户区，标题栏，菜单，边框
    hWndDC = win32gui.GetWindowDC(0)
    # 创建设备描述表
    mfcDC = win32ui.CreateDCFromHandle(hWndDC)
    # 创建内存设备描述表
    saveDC = mfcDC.CreateCompatibleDC()
    # 创建位图对象准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    # 为bitmap开辟存储空间
    saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)
    # 将截图保存到saveBitMap中
    saveDC.SelectObject(saveBitMap)
    # 保存bitmap到内存设备描述表
    saveDC.BitBlt((0, 0), (width, height), mfcDC, (left, top), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, global_.test_img)
    return react


def move_click(point):
    pos = win32api.GetCursorPos()
    win32api.SetCursorPos(point)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    win32api.SetCursorPos(pos)

def reset_windows_size():
    hWnd = win32gui.FindWindow(None, '阴阳师-网易游戏')
    win32gui.SetWindowPos(hWnd, win32con.HWND_NOTOPMOST, -7, 0, 1000, 1, win32con.SWP_SHOWWINDOW)
    print("reset_windows_size")


