import sys
import os

print(os.path.realpath(sys.argv[0]) + "\\")
print(os.path.realpath(sys.executable))
print(os.path.dirname(os.path.realpath(sys.argv[0])))
print(os.path.dirname(os.path.realpath(sys.executable)))


import time

i = 0
while True:
    print(i)
    i = i+1
    time.sleep(0.02)