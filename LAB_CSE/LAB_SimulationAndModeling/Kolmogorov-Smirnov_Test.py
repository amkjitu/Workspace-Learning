from scipy.stats import kstest
import random
from scipy import stats
import scipy.stats

'''
# N = int(input("Enter number of random numbers: "))
N = 5

actual =[]
print("Enter outcomes: ")
for i in range(N):
	# x = float(input("Outcomes of class "+str(i + 1)+": "))
	actual.append(random.random())

print(actual)
x = kstest(actual, "uniform")
print(x)

for i in range(10):
	x = random.randint(0,1)
	print(x)

for i in range(10):
	x = random.uniform(0,1)
	print(x)
'''

alpha = float(input("Enter the value of alpha: "))
critical = float(input("Enter the critical value of alpha: "))
randNumbers = list(map(float, input("Enter the random numbers: ").split(' ')))
noOfNumbers = len(randNumbers)

#print(randNumbers)
#print(noOfNumbers)

ibNmRi = []
Rimim1bN = []

for i in range(noOfNumbers):
	j = i + 1
	ibN = j/noOfNumbers
	ibNmRi.append((ibN - randNumbers[i]))
	Rimim1bN.append((randNumbers[i]-((j-1)/noOfNumbers))) 

#0.11 0.23 0.24 0.41 0.50 0.61 0.64 0.65 0.86 0.89

Dplus = max(ibNmRi)
Dminus = max(Rimim1bN)
D = (max(Dplus,Dminus))

print("D+ : {}".format(Dplus))
print("D- : {}".format(Dminus))

if(critical > D):
	print("Uniform")
else: print("Not Uniform")

#print(max(ibNmRi))
#print(max(Rimim1bN))

#print("Critical value")
#crit = scipy.stats.f.ppf(cl=1-0.05, dfn=9, dfd=9)
#print(crit)

'''
dfn denotes number of degrees of freedom that the estimate of variance used in the numerator.
dfd is the number of degrees of freedom that the estimate of variance used in the denominator.
dfn = a-1
dfd = N-a
where a is the number of groups and N is the total number of subjects in the experiment.
The shape of the F distribution depends on dfn and dfd. The lower the degrees of freedom, 
the larger the value of F needed to be significant.
'''

	