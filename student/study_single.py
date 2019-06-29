
# coding:utf-8

import signal
import time

def handler(signum, frame):
    print('Got signal: ', signum)


signal.signal(signal.SIGINT, handler)

time.sleep(10)
print('params end')