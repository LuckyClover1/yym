import json
from class_ import module
import tkinter

print(" python applicatio started....")
f =open('resource/zudui/yuhun.json',encoding='utf-8') #打开‘product.json’的json文件
res=f.read()  #读文件
dict_arr = json.loads(res)
print("read yuhun.json ....")
index = 0
length = len(dict_arr)
while (1):
    action = dict_arr[index]["action"]
    template = dict_arr[index]["template"]
    match = dict_arr[index]["match"]
    tryTimes = dict_arr[index]["tryTimes"]
    team_num = dict_arr[index]["team_num"]
    obj = module(action,template,match,tryTimes,team_num)
    func = getattr(obj,obj.action)
    func()
    index = index + 1
    if index == length:
        index = 0
