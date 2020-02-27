from pynput.keyboard import Key,Listener

last = Key.esc
def on_press(key):
    global last
    if key == Key.ctrl_l and last != Key.ctrl_l:
        last = key
    elif last == Key.ctrl_l and key == Key.alt_l:
        return False #按键不是enter,停止监视
    else:
        last = key

def on_release(key):
    pass
#监听键盘按键
def start_listener():
    print('please enter ctrl + alt exit')
    with Listener(on_press=on_press,on_release=on_release) as listener:
        listener.join()
    #停止监视
    Listener.stop()

