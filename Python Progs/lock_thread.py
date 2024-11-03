# The lock helps us in the synchronization of two or more threads.
# it has two primary methods: acquire() and release().


import threading

lock = threading.Lock()
deposit = 50


def add_profit():  # Function to add profit to the profit
    global deposit
    for i in range(100000):
        lock.acquire()  # acquire the lock
        deposit = deposit + 10
        lock.release()  # free the acquired lock


def pay_bill():  # Function to deduct money from the deposit
    global deposit
    for i in range(100000):
        lock.acquire()
        deposit = deposit - 10
        lock.release()


thread1 = threading.Thread(target=add_profit, args=())
thread2 = threading.Thread(target=pay_bill, args=())
# starting the threads
thread1.start()
thread2.start()
# waiting for both the threads to finish executing
thread1.join()
thread2.join()
print(deposit)
