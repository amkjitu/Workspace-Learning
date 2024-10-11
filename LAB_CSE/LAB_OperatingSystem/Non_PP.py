from multiprocessing import Process
import multiprocessing
import threading
import time
import os
import random

# Python3 program for implementation
# of FCFS scheduling

def Task(process_no,burst_time):
	print("\t\t\tProcess No.{} \t PID: {} Execution Started".format(process_no,os.getpid()))
	for i in range(burst_time):
		print("\t\t\tProcess No.{} \t PID: {} Execution Running TIME: {}".format(process_no,os.getpid(),i+1))
		time.sleep(1)
	print("\t\t\tProcess No.{} \t PID: {} **Execution Finished**".format(process_no,os.getpid()))

# Function to find the waiting
# time for all processes
def findWaitingTime(processes, n, bt, tat, wt):
	# waiting time for
	# calculating waiting time
	for i in range(n):
		wt[i] = tat[i] - bt[i]

# Function to calculate turn
# around time
def findTurnAroundTime(processes, n, at , ct, tat):
	# calculating turnaround
	# time by adding bt[i] + wt[i]
	for i in range(n):
		tat[i] = at[i] + ct[i]

def findCompletionTime(processes, n, bt, ct):
	# calculating Completion
	# time by adding ct[i] + bt[i]

	ct[0] = bt[0]
	for i in range(1,n):
		ct[i] =  ct[i-1] + bt[i]

def findResponseTime(processes, n, at, wt, rt):
	# calculating Completion
	# time by adding wt[i] - at[i]
	for i in range(1,n):
		rt[i] =  wt[i] - at[i]



# Function to calculate
# average time
def PP(processes, n, prio , at ,bt):

	#Priority onujayi sorted process and burst time sort kori
	for i in range(n):
		for k in range(i+1,n):
			if(prio[i]<prio[k]):
				temp=prio[i];
				prio[i]=prio[k];
				prio[k]=temp;
				
				temp=processes[i];
				processes[i]=processes[k];
				processes[k]=temp;

				temp=bt[i];
				bt[i]=bt[k];
				bt[k]=temp;


	#for i in range(n):
		#print("p{} b{}".format(processes[i],bt[i]))

	wt = [0] * n
	tat = [0] * n
	ct = [0] * n
	rt = [0] * n
	total_wt = 0
	total_tat = 0

	# Function to find completion time for all processes
	findCompletionTime(processes, n, bt, ct)

	# Function to find turn around time for all processes
	findTurnAroundTime(processes, n, at, ct, tat)

	# Function to find waiting time of all processes
	findWaitingTime(processes, n, bt, tat, wt)

	# Function to find response time of all processes
	findResponseTime(processes, n, at, wt, rt)

	# Display processes along 
	# with all details
	print( "Processes  " + "Prority  " + "Arrival time"+" Burst time " +"Completion time"+ " Turn around time " + " Waiting time" + " Response time")

	# Calculate total waiting time
	# and total turn around time
	for i in range(n):
		total_wt = total_wt + wt[i]
		total_tat = total_tat + tat[i]
		process = Process(target=Task, args=(processes[i],burst_time[i],))
		process.start()
		process.join()
		print(" " + str(processes[i])+ "\t    " + str(prio[i])+ "\t    " + str(at[i]) + "\t\t "  + str(bt[i]) + "\t\t" + str(ct[i]) + "\t\t" + str(tat[i]) + "\t\t" + str(wt[i])+ "\t\t" + str(rt[i]))
		
	print( "Average waiting time = "+ str(total_wt / n))
	print("Average turn around time = "+ str(total_tat / n))

# Driver code
if __name__ == "__main__":
	
	# process id's
	#processes = [ 1, 2, 3, 4, 5 ]
	#n = len(processes)

	noOfProcess = int(input("Enter the number of process: "))
	process = []
	for i in range(1,noOfProcess+1):
		process.append(i)
		# Burst time of all processes
	burst_time = [5,3,1,7,4]
	arrival_time = [0, 0, 0, 0, 0]
	prority = [4, 1, 2, 2, 3]

	PP(process, noOfProcess, prority, arrival_time, burst_time)

