import json
import global_


def read_json(file):
    file = global_.local + file
    print("read ", file)
    f = open(file, encoding='utf-8')  # 打开‘product.json’的json文件
    res = f.read()  # 读文件
    return json.loads(res)
