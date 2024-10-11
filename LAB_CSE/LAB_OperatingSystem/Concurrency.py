import threading
import time
import os

def task1():
	print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
	print("ID of process running task 1: {}".format(os.getpid()))
	time.sleep(2)
	for i in range(100):
		print("Task 1: {}".format(i))
		time.sleep(0.1)
	print("Task 1 Process ID: {} Finished".format(os.getpid()))

def task2():
	print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
	print("ID of process running task 2: {}".format(os.getpid()))
	time.sleep(5)
	for i in range(100):
		print("Task 2: {}".format(i))
	print("Task 2 Process ID: {} Finished".format(os.getpid()))

if __name__ == "__main__":

	# print ID of current process
	print("ID of process running main program: {}".format(os.getpid()))

	# print name of main thread
	print("Main thread name: {}".format(threading.current_thread().name))

	# creating threads
	t1 = threading.Thread(target=task1, name='t1')
	t2 = threading.Thread(target=task2, name='t2')

	# starting threads
	t1.start()
	print(threading.activeCount())
	t2.start()
	print(threading.activeCount())

	# wait until all threads finish
	t1.join()
	t2.join()

	print("No Thread")
	#task1()
	#print("Duration of Task 1 without thread: {}".format(threading.activeCount()))
	#task2()
	#print("Duration of Task 1 without thread: {}".format(threading.activeCount()))





'''
import threading
import time


def func():
    print('ran')
    time.sleep(1)
    print("done")
    time.sleep(2)
    print("now done",end=" ")


x = threading.Thread(target=func)
x.start()
print(threading.activeCount())
time.sleep(5)
print("finally\n")
'''