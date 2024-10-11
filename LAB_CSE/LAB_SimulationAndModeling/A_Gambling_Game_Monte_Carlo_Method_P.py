import random as rand
import matplotlib.pyplot as plt
import numpy as np

gamePrize  = 8
totalMoneyPaid = 0
game = int(input("Enter the no of games: "))

for i in range(1,game+1):
    countH = 0
    countT = 0
    countFlip = 0

    while(1):
        countFlip += 1

        coinFlip = rand.randint(0,9) # 0 1 2 3 4 5 6 7 8 9

        if coinFlip >= 0 and coinFlip <= 4:
            countT += 1
        else:
            countH += 1
    
        difHandT = abs(countH-countT)
       
        if(difHandT == 3):
            totalMoneyPaid += countFlip
            break

print("Average requires {} filps".format(totalMoneyPaid/game))
