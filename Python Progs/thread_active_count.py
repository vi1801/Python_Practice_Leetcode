import time
import threading
from threading import Thread


def sleepThread(x):
    print("Thread %x going to sleep for 2 seconds" % x)
    time.sleep(2)
    print("Thread %x is active now." % x)


for x in range(10):
    th = Thread(target=sleepThread, args=(x, ))
    th.start()
    print("Current Thread Count: %x." % threading.active_count())

print(threading.main_thread())
