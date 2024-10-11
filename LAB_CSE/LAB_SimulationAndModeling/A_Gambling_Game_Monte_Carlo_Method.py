import random as rand
import matplotlib.pyplot as plt
import numpy as np

countWin = 0
countLose = 0
gamePrize  = 8
totalMoneyPaid = 0
totalWonMoney = 0
totalLossedMoney = 0

listwinningprize = []
listlossinggprize = []

game = int(input("Enter the no. of game You want to play : "))
print("\n___________________________________________________________________________________________")
print("{:^12}{:^10}{:^20}{:^15}{:^20}{:^15}".format("Game No.", "SL No.", "Random Number", "Head/Tail", "Cummulative", "Difference"))
print("{:^12}{:^10}{:^20}{:^15}{:^20}{:^15}".format("", "", "", "", "-----------------", ""))
print("{:^12}{:^10}{:^20}{:^15}{:^20}{:^15}".format("", "", "", "", "Heads   Tails", ""))
print("___________________________________________________________________________________________")

for i in range(1,game+1):
    countH = 0
    countT = 0
    countFlip = 0
    prizeWin = 0
    prizeLose = 0
    print("{:^12}".format(i),end='')

    while(1):
        countFlip += 1
        if(countFlip>1):
            print("{:^12}{:^10}".format("",countFlip),end='')
        else:
            print("{:^10}".format(countFlip),end='')

        coinFlip = rand.randint(0,9) # 0 1 2 3 4 5 6 7 8 9
        print("{:^20}".format(coinFlip),end='')

        if coinFlip >= 0 and coinFlip <= 4:
            print("{:^15}".format("T"),end='')
            countT += 1
            #print("{:^20}".format(countT),end='')
        else:
            print("{:^15}".format("H"),end='')
            countH += 1
            #print("{:^20}".format(countH),end='')

        print("{:^9}{:^9}".format(countH,countT),end='')

        #print("H = {}, T={}".format(countH,countT))
        difHandT = abs(countH-countT)
        print("{:^15}".format(difHandT),end ='')
        print()
        if(difHandT == 3):
            totalMoneyPaid += countFlip

            if(gamePrize - countFlip > 0):
                countWin += 1
                prizeWin = gamePrize - countFlip
                listwinningprize.append(prizeWin) #extra kori
                totalWonMoney += prizeWin
                text = "/\/  In Game no. {} wins {} tk  /\/".format(i,prizeWin)
                print("{:^90}\n".format(text))
                #print("~~~~~~~~~~~ In Game no. {} He woned {} tk  ~~~~~~~~~~~\n".format(i,prizeWin))
            elif(gamePrize - countFlip < 0):
                countLose += 1
                prizeLose = abs(gamePrize - countFlip)
                listlossinggprize.append(prizeLose) #extra kori
                totalLossedMoney += prizeLose
                text = "/\/  In Game no. {} loses {} tk  /\/".format(i,prizeLose)
                print("{:^90}\n".format(text))
                #print("~~~~~~~~~~~ In Game no. {} He lossed {} tk  ~~~~~~~~~~~\n".format(i,prizeLose))
            break

print("________________________________________Game Summary_______________________________________")
print("Total wins {} games".format(countWin))
print("Total loses {} games".format(countLose))

if(totalWonMoney > totalLossedMoney):
    print("Won {} tk after playing {} games".format(totalWonMoney - totalLossedMoney,game))
elif(totalWonMoney < totalLossedMoney):
    print("Lost {} tk after playing {} games".format(abs(totalWonMoney - totalLossedMoney),game))
else:
     print("The game drawn after playing {} games".format(game))

print("Total money paid {}".format(totalMoneyPaid))
print("Each game on average requires {} filps".format(totalMoneyPaid/game))
print("___________________________________________________________________________________________")

#print("Wins: {}".format(listwinningprize))
#print("Loses: {}".format(listlossinggprize))

listwinningprize.sort()
listlossinggprize.sort()

max1 = listwinningprize[-1]
max2 = listlossinggprize[-1]

max = 0
if max1>max2:
    max = max1
else:
    max = max2


plt.style.use('ggplot')

plt.subplot(1, 2, 1)
bins1 = np.linspace(0, max1, 10)
plt.title("Amount of times VS Amount of Money")
plt.xlabel("Money")
plt.ylabel("Times")
plt.hist(listwinningprize, bins1, color = "green", alpha=0.75, label='Wins')
#plt.legend(loc='upper right')
plt.legend()

plt.subplot(1, 2, 2)
bins2 = np.linspace(0, max2, 10)
plt.title("Amount of times VS Amount of Money")
plt.xlabel("Money")
plt.ylabel("Times")
plt.hist(listlossinggprize, bins2, color = "red", alpha=0.75, label='Loses')
plt.legend()
#plt.legend(loc='upper right')
plt.show()

'''
bins = np.linspace(0, max, 10)
plt.xlabel("Amount of Money")
plt.ylabel("Amount of Times")
plt.hist(listwinningprize, bins, alpha=0.5, label='Wins')
plt.hist(listlossinggprize, bins, alpha=0.5, label='Loses')
plt.legend()
#plt.legend(loc='upper right')
plt.show()
'''
