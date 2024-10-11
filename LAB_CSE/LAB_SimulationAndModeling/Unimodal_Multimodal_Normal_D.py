# Importing required libraries
'''
A probability distribution is a statistical function that describes the likelihood of obtaining the possible values that 
a random variable can take. By this, we mean the range of values that a parameter can take when we randomly pick up values 
from it.

A Normal Distribution is also known as a Gaussian distribution or famously Bell Curve. 
People use both words interchangeably, but it means the same thing. It is a continuous probability distribution.

The probability density function (pdf) for Normal Distribution:

'''

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from scipy.stats import binom
from numpy import random

###UniModal Density Function
 
# Creating a series of data of in range of 1-50.
x = np.linspace(1,50,200)

#print(x)
 
#Creating a Function.
def normal_dist(x , mean , sd):
    #prob_density = (np.pi*sd) * np.exp(-0.5*((x-mean)/sd)**2)
    prob_density = (1/((2*np.pi)**0.5 *sd)) * np.exp(-0.5*((x-mean)/sd)**2)
    return prob_density
 
#Calculate mean and Standard deviation.
mean = np.mean(x)
sd = np.std(x)
 
#Apply function to the data.
pdf = normal_dist(x,mean,sd)
 
#Plotting the Results
plt.plot(x,pdf , color = 'red')
plt.xlabel('Data points')
plt.ylabel('Probability Density')
plt.show()

###Multimodal Density Function
#here we are using multinomial function to generate distributions of size 1000 with 3 outcomes each having probability 1/3
sb.distplot(random.multinomial(size=1000,n=3,pvals=[1/3,1/3,1/3]), hist=True, label='normal')
#plotting the graph
plt.show()

###To generate a random sample with a sample size of 200, which follows a normal distribution 
###with a mean of 100 and a standard deviation of 20
SampleSize = 200
mean = 100
sd = 20
RandomSample = np.random.normal(mean, sd, SampleSize)
print("Random Sample: {}".format(RandomSample))

#The distribution of diastolic blood pressure for men is normally distributed with a mean of about 80 and 
#a standard deviation of 20.
SampleSize = 200
mean = 80
sd = 20
RandomSample = np.random.normal(mean, sd, SampleSize)
print("Random Sample: {}".format(RandomSample))
plt.hist(RandomSample)
plt.show()



'''
###Multimodal Density Function
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
 
# Creating a series of data of in range of 1-50.
x = np.linspace(1,50,50)
x1 = np.linspace(20,80,60)
x2 = np.linspace(10,100,90)

X = np.concatenate([x, x1, x2])

print(x)
print(x1)
print(x2)
print(X)
 
#Creating a Function.
def normal_dist(X , mean , sd):
    prob_density = (np.pi*sd) * np.exp(-0.5*((X-mean)/sd)**2)
    #prob_density = (1/((2*np.pi)**0.5 *sd)) * np.exp(-0.5*((x-mean)/sd)**2)
    return prob_density
 
#Calculate mean and Standard deviation.
mean = np.mean(X)
sd = np.std(X)
 
#Apply function to the data.
pdf = normal_dist(X,mean,sd)
 
#Plotting the Results
plt.plot(X, pdf , color = 'red')
plt.xlabel('Data points')
plt.ylabel('Probability Density')
plt.show()


N=400
mu, sigma = 100, 5
mu2, sigma2 = 10, 40
X1 = np.random.normal(mu, sigma, N)
X2 = np.random.normal(mu2, sigma2, N)
X = np.concatenate([X1, X2])
count, bins, ignored = plt.hist(X)
plt.plot(bins,X)
plt.show()

'''

'''
import matplotlib.pyplot as plt
from scipy.stats import binom
# setting the values
# of n and p
n = 100
p = 0.6
# defining list of r values
r_values = list(range(n + 1))
# list of pmf values
dist = [binom.pmf(r, n, p) for r in r_values ]
# plotting the graph
plt.bar(r_values, dist)
plt.plot(r_values, dist)
plt.show()
'''


'''
###
 
# Creating a series of data of in range of 1-50.
#x = np.linspace(1,50,200)

# Creating a series of data of in range of 100.
mean, sd = 100, 20
x = np.random.normal(mean, sd, 200)

print(x)
 
#Creating a Function.
def normal_dist(bins , mean , sd):
    #prob_density = (np.pi*sd) * np.exp(-0.5*((x-mean)/sd)**2)
    prob_density = 1/(sd * np.sqrt(2 * np.pi)) * np.exp( - (bins - mean)**2 / (2 * sd**2) )
    return prob_density
 
#Calculate mean and Standard deviation.
#mean = np.mean(x)
#sd = np.std(x)
 
#Apply function to the data.
#pdf = normal_dist(x,mean,sd)
#pdf = normal_dist(x,mean,50)
 
#Plotting the Results
#plt.plot(x,pdf , color = 'red')
#plt.xlabel('Data points')
#plt.ylabel('Probability Density')
#plt.show()

#Plotting the Results
count, bins, ignored = plt.hist(x, 30, density=True)
#print(bins)
#plt.plot(bins, normal_dist(bin , mean , sd), linewidth=2, color='r')
plt.plot(bins, 1/(sd * np.sqrt(2 * np.pi)) * np.exp( - (bins - mean)**2 / (2 * sd**2) ) ,linewidth=2, color='r')
plt.show()
'''