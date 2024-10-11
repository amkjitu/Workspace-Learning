from logging import CRITICAL
import numpy as np
import pandas as pd
import scipy.stats as stats
import random
'''

national = pd.DataFrame(["white"] * 100000 + ["hispanic"] * 60000 + \
                        ["black"] * 50000 + ["asian"] * 15000 + ["other"] * 35000)

minnesota = pd.DataFrame(["white"] * 600 + ["hispanic"] * 300 + \
                         ["black"] * 250 + ["asian"] * 75 + ["other"] * 150)

national_table = pd.crosstab(index=national[0], columns="count")
minnesota_table = pd.crosstab(index=minnesota[0], columns="count")

print("National")
print(national_table)
print(" ")
print("Minnesota")
print(minnesota_table)
observed = minnesota_table

national_ratios = national_table/len(national)  # Get population ratios

expected = national_ratios * len(minnesota)   # Get expected counts

chi_squared_stat = (((observed-expected)**2)/expected).sum()

print(chi_squared_stat)
crit = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 4)   # Df = number of variable categories - 1

print("Critical value")
print(crit)

# Find the p-value
p_value = 1 - stats.chi2.cdf(x=chi_squared_stat,df=4)
print("P value = ")
print(p_value)
stats.chisquare(f_obs= observed,   # Array of observed counts
                f_exp= expected)
'''


noOfRandomNumber = int(input("Enter the number of random number: "))
alpha = float(input("Enter the value of alpha: "))
critical = float(input("Enter the critical value of alpha: "))

randomNumbers = []
for i in range(1,noOfRandomNumber+1):
    R = random.randint(1,100)
    randomNumbers.append(R)

print("{} {:^20} {:^20} {:^20} {:^20}".format("Classes", "Count", "Frequency", "Diff", "Diff^2"))
classp = 1
count = 0
SofDiffS = 0
for i in range(10):
    classn = (i+1) * 10
    for i in range(noOfRandomNumber):
        if(randomNumbers[i]>classp and randomNumbers[i]<=classn):
            count = count + 1
    cou = '*' * count
    #Diff = frequency - (noOfRandomNumber/Classes)
    Diff = count-(noOfRandomNumber/10)
    DiffS = Diff*Diff
    SofDiffS = SofDiffS + DiffS
    print("{}-{} {:^25} {:^20} {:^20} {:^20}".format(classp,classn, cou, count, Diff, DiffS))
    classp = classn
    count = 0



print("Chi-Square: {}/{} = {}".format(SofDiffS,10,SofDiffS/10))
Chi_Square = SofDiffS/10
if(critical>Chi_Square):
    print("Uniform")
else: print("Not Uniform")


