from multiprocessing import Process
import multiprocessing
import threading
import time
import os
import random

def Task_1(process_name,burst_time):
    time.sleep(burst_time)
    print('Process Name: ' + " " + process_name)
    print("ID of process running task 1: {}".format(os.getpid()))
    print("Process ID: {} finisted by : {}\n".format(os.getpid(), burst_time))

def Task_2(process_name,burst_time):
    time.sleep(burst_time)
    print('Process Name: ' + " " + process_name)
    print("ID of process running task 2: {}".format(os.getpid()))
    print("Process ID: {} finisted by : {}\n".format(os.getpid(), burst_time))

def Task(process_no,burst_time):
    print("Process No: {} \t PID: {}".format(process_no,os.getpid()))
    time.sleep(burst_time)
    print("{} Process ID: {} finisted by : {}\n".format(process_no,os.getpid(), burst_time))


if __name__ == '__main__':
    #ekhane 2 ta process create korsi
    #burstTime_1 = random.choice(range(1,5))
    #burstTime_2 = random.choice(range(1,5))
    #p1 = Process(target=Task_1, args=('Process_1',burstTime_1,))
    #p2 = Process(target=Task_2, args=('Process_2',burstTime_2,))
    #p1.start()
    #p2.start()
    #p1.join()
    #p2.join()

    #ekhane n ta process create korsi
    processes = []
    noOfProcess = int(input("Enter the number of process: "))
    for i in range(1, noOfProcess+1):
        process_no = i
        burst_time = random.choice(range(1,6))
        process = Process(target=Task, args=(process_no,burst_time,))
        processes.append(process)
        #process.start()
        
    for proc in processes:
        proc.start()
        proc.join()