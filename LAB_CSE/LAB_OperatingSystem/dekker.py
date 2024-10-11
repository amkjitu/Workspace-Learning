def Thread1():
	doWhile=False
	while not completed or not doWhile:
		doWhile=True
		# entry section
		# wait until threadnumber is 1
		while (threadnumber == 2):
			pass

		# critical section

		# exit section
		# give access to the other thread
		threadnumber = 2

		# remainder section

def Thread2():
	doWhile=False
	while not completed or not doWhile:
		doWhile=True
		# entry section
		# wait until threadnumber is 2
		while (threadnumber == 1):
			pass

		# critical section

		# exit section
		# give access to the other thread
		threadnumber = 1

		# remainder section

if __name__ == '__main__':

	thread_number = 1
	startThreads()
