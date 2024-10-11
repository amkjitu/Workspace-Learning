# Importing required libraries
'''
A probability distribution is a statistical function that describes the likelihood of obtaining the possible values that 
a random variable can take. By this, we mean the range of values that a parameter can take when we randomly pick up values 
from it.

A Normal Distribution is also known as a Gaussian distribution or famously Bell Curve. 
People use both words interchangeably, but it means the same thing. It is a continuous probability distribution.


'''

'''
import numpy as np
import matplotlib.pyplot as plt
 
# Creating a series of data of in range of 1-50.
x = np.linspace(1,50,200)

print(x)
 
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

'''

import numpy as np
import matplotlib.pyplot as plt
 
# Creating a series of data of in range of 1-50.
#x = np.linspace(1,50,200)

# Creating a series of data of in range of 100.
mean, sd = 100, 20
x = np.random.normal(mean, sd, 200)

print(x)
 
#Creating a Function.
def normal_dist(bin , mean , sd):
    #prob_density = (np.pi*sd) * np.exp(-0.5*((x-mean)/sd)**2)
    prob_density = 1/(sd * np.sqrt(2 * np.pi)) * np.exp( - (bins - mean)**2 / (2 * sd**2) )
    return prob_density
 
#Calculate mean and Standard deviation.
#mean = np.mean(x)
#sd = np.std(x)
 
#Apply function to the data.
#pdf = normal_dist(x,mean,sd)
pdf = normal_dist(x,mean,50)
 
#Plotting the Results
#plt.plot(x,pdf , color = 'red')
#plt.xlabel('Data points')
#plt.ylabel('Probability Density')
#plt.show()

#Plotting the Results
count, bins, ignored = plt.hist(x, 30, density=True)
#print(bins)
plt.plot(bins, normal_dist(bin , mean , sd), linewidth=2, color='r')
#plt.plot(bins, pdf ,linewidth=2, color='r')
plt.show()