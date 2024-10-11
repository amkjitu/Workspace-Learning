import threading, time, random

mutex = threading.Lock()


class thread_one(threading.Thread):
    def run(self):
        global mutex
        print("The first thread is now sleeping")
        time.sleep(random.randint(1, 5))
        print("First thread is finished")
        mutex.release()


class thread_two(threading.Thread):
    def run(self):
        global mutex
        print("The second thread is now sleeping")
        time.sleep(random.randint(1, 5))
        mutex.acquire()
        print("Second thread is finished")


mutex.acquire()
t1 = thread_one()
t2 = thread_two()
t1.start()
t2.start()