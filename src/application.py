from module import Module
import ui
from file_func import *
import global_
import time

print(" python application started....")
dict_arr = read_json(global_.config)
index = 0
length = len(dict_arr)
ui.reset_windows_size()
on = True
while on:
    # 获取配置
    action = dict_arr[index]
    # 创建类
    obj = Module(action["action"], action["template"], action["team_num"])
    # 获取对应的方法
    func = getattr(obj, obj.action)
    # 执行
    func()
    
    index = index + 1
    # 配置文件结束，循环
    if index == length:
        index = 0
        # time.sleep(60)
