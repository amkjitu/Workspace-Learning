import numpy as np
import pandas as pd
desired_width = 320
pd.set_option("display.width",desired_width)
pd.set_option("display.max_columns",None)
pd.set_option("display.max_rows",None)
np.set_printoptions(linewidth=desired_width)
def GenerateLifeInHours(NumerofReplacement):
    bearing = list()
    Random_Digit = list()
    for N in range(NumerofReplacement):
        r_n = np.random.randint(0,100)
        if r_n in range(1,11):
            lifecycle = 1000
            bearing.append(lifecycle)
            Random_Digit.append(r_n)
        elif r_n in range(11,25):
            lifecycle = 1100
            bearing.append(lifecycle)
            Random_Digit.append(r_n)
        elif r_n in range(25,49):
            lifecycle = 1200
            bearing.append(lifecycle)
            Random_Digit.append(r_n)
        elif r_n in range(49,63):
            lifecycle = 1300
            bearing.append(lifecycle)
            Random_Digit.append(r_n)
        elif r_n in range(63,75):
            lifecycle = 1400
            bearing.append(lifecycle)
            Random_Digit.append(r_n)
        elif r_n in range(75,85):
            lifecycle = 1500
            bearing.append(lifecycle)
            Random_Digit.append(r_n)
        elif r_n in range(85,91):
            lifecycle = 1600
            bearing.append(lifecycle)
            Random_Digit.append(r_n)
        elif r_n in range(91,96):
            lifecycle = 1700
            bearing.append(lifecycle)
            Random_Digit.append(r_n)
        elif r_n in range(96,99):
            lifecycle = 1800
            bearing.append(lifecycle)
            Random_Digit.append(r_n)
        elif r_n in [99,0]:
            lifecycle = 1900
            bearing.append(lifecycle)
            Random_Digit.append(r_n)
    return bearing,Random_Digit

def GenerateDelayTime(NumerofReplacement):
    DelayTime = list()
    Random_Digit = list()
    for N in range(NumerofReplacement):
        r_n = np.random.randint(0, 10)
        if r_n in range(1, 4):
            delay_time = 4
            DelayTime.append(delay_time)
            Random_Digit.append(r_n)
        elif r_n in range(4, 10):
            delay_time = 6
            DelayTime.append(delay_time)
            Random_Digit.append(r_n)
        elif r_n == 0:
            delay_time = 8
            DelayTime.append(delay_time)
            Random_Digit.append(r_n)

    return DelayTime, Random_Digit
#bearing life
bearing1_life, RD1 = GenerateLifeInHours(25)
bearing2_life,RD2 = GenerateLifeInHours(25)
bearing3_life,RD3 = GenerateLifeInHours(25)
#delay time
DelayTime, RD_DealayTime = GenerateDelayTime(25)

cum_sum = 0
first_failure = list()
CummulatedLife = list()
for i in range(25):
    failure = np.min(list((bearing1_life[i],bearing2_life[i],bearing3_life[i])))
    cum_sum += failure
    CummulatedLife.append(cum_sum)
    first_failure.append(failure)

df = pd.DataFrame({"RD1": RD1 , "Bearing 1 Life (Hrs.)": bearing1_life, "RD2": RD2 ,
                   "Bearing 2 Life (Hrs.)": bearing2_life, "RD3": RD3,"Bearing 3 Life (Hrs.)": bearing3_life,
                   "First Failure (Hrs.)": first_failure,"Cumulated Life (Hrs.)": CummulatedLife,
                   "RD_DelayTime": RD_DealayTime, "Delay (Minutes)": DelayTime})
print(f"Total Delay Time: {np.sum(DelayTime)}")
print(f"Total Number of Replacement: 25\nRequiring a total of {25*3} bearings")
print(f"Time spent in Changing the bearings: {25*40} minutes")
print(f"Total Downtime: {np.sum(DelayTime) + 25*40}")
print(f"Cost of Bearings = 75*20 = {75*20}")
print(f"Cost of Downtime = {np.sum(DelayTime) + 25*40}*5 = {(np.sum(DelayTime) + 25*40) * 5}")
print(f"Cost of Repairman = {25*40}*{np.round(25/60, 2)} = {np.round((25*40)*(25/60),2)}")
total_cost = (75*20)+((np.sum(DelayTime) + 25*40) * 5)+((25*40)*(25/60))
total_cost = np.round(total_cost,2)
print(F"Total Cost: {total_cost}")
print("-"*70)
print(df)