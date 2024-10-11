

BearingLife = {}
BearingLife[1000] = 0.10
BearingLife[1100] = 0.14
BearingLife[1200] = 0.24
BearingLife[1300] = 0.14
BearingLife[1400] = 0.12
BearingLife[1500] = 0.10
BearingLife[1600] = 0.06
BearingLife[1700] = 0.05
BearingLife[1800] = 0.03
BearingLife[1900] = 0.02

preran = 1
csum = 0
CumuProbability = {}
CumuProbability[1000] = BearingLife[1000]
RandomdigitAssignmentforLife = []
RandomdigitAssignmentforLife.append(1900)
for i in range(1000,1901,100):
    csum += BearingLife[i];
    #CumuProbability.append((CumuProbability[i]+csum))
    CumuProbability[i] = 0 
    CumuProbability[i]=CumuProbability[i]+csum

    upperRan = int(CumuProbability[i]*100)
    for j in range(preran, upperRan):
        RandomdigitAssignmentforLife.append(i)
        preran = j
    preran += 1

    print("Bearing Life (Hours) = {}, Probability {}, Cumulative Probablity = {}".format(i,BearingLife[i],CumuProbability[i]))

for i in range(len(RandomdigitAssignmentforLife)):
    print("{} = {} ".format(i,RandomdigitAssignmentforLife[i]))

n = 62
for i in range(100):
    if(n==i):
        print("for random number {} the hour = {}".format(n,RandomdigitAssignmentforLife[i]))

DelayTime = {}
DelayTime[4] = 0.3
DelayTime[6] = 0.6
DelayTime[8] = 0.1

preran = 1
csumHr = 0
CumuProbabilityHr = {}
CumuProbabilityHr[4] = DelayTime[4]
RandomdigitAssignmentforDelay = []
RandomdigitAssignmentforDelay.append(8)
for i in range(4,9,2):
    csumHr += DelayTime[i];
    #CumuProbability.append((CumuProbability[i]+csum))
    CumuProbabilityHr[i] = 0 
    CumuProbabilityHr[i]=CumuProbabilityHr[i]+csumHr

    upperRan = int(CumuProbabilityHr[i]*10)
    for j in range(preran, upperRan):
        RandomdigitAssignmentforDelay.append(i)
        preran = j
    preran += 1
    print("Delay (Hours) = {}, Probability {}, Cumulative Probablity = {}".format(i,DelayTime[i],CumuProbabilityHr[i]))

for i in range(len(RandomdigitAssignmentforDelay)):
    print("{} = {} ".format(i,RandomdigitAssignmentforDelay[i]))








