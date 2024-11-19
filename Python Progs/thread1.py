import threading
import time
from time import sleep


def cal_square(numbers):
    for n in numbers:
        sleep(0.2)
        print('square:', n * n)


def cal_cube(numbers):
    for n in numbers:
        sleep(0.2)
        print('cube', n * n * n)


arr = [2, 3, 8, 9]
t = time.time()
t1 = threading.Thread(target=cal_square, args=(arr,))
t2 = threading.Thread(target=cal_cube, args=(arr,))

t1.start()  # start the thread
# sleep(0.2)  # sleep to avoid collision
t2.start()
t1.join()  # wait till t1 and t2 are done
t2.join()
print("Bye")  # main thread print bye

print("done in: ", time.time() - t)


