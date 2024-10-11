import time
import numpy as np
import pandas as pd
import urllib.request as urlreq

def cpuBegin():
    # get the start time
    st = time.process_time()
    return st

def cpuEnd():
   # get the start time
   et = time.process_time()
   return et

##this is a generic list in python likewise array
arr1 = [0.1,0.2,0.3]
arr2 = [10,20,30]

##list to np arraay
nparr1 = np.array(arr1)
nparr2 = np.array(arr2)

##np.arange(start,stop,step) => a range from start upto stop of step size
numrange = np.arange(0,10,2)
print(numrange)

##np.linespace(start,stop,indices) => creates a range from start to stop of n points
numpoints = np.linspace(0,1,10)
print(numpoints)

##np.random.randint(low,high,shape) a random number from low upto high of shape 
numrandom = np.random.randint(0,10,5)
print(numrandom)
numrandom = np.random.randint(0,10,(3,3))
print(numrandom)

##np.random.randint(low,high,shape) a fixed random number from low upto high of shape 
np.random.seed(101) #seed should be in the same cell
numrandom = np.random.randint(0,10,(3,3))
print(numrandom)

##np.random.randint(low,high,shape) a random number of gausian distribution from low upto high of shape 
numrandom = np.random.normal(1,10,10)
print(numrandom)

##arr.min() => gets the min element
print(nparr2.min())
##arr.max() => gets the max element
print(nparr2.max())
##arr.min() => gets the index of min element
print(nparr2.argmin())
##arr.min() => gets the index of max element
print(nparr2.argmax())

##np.reshape(n,m) => creates a matrix of n rows and m columns
nparr3 = np.array([1,2,3,4,5,6,7,8,9,10]) 
reshapednparray3 = nparr3.reshape(2,5)
print(nparr3)
print(reshapednparray3)

##create a matrix of 10 x 10 using np.arange and reshape
mat = np.arange(0,100).reshape(10,10)
print(mat)
#index wise value of the matrix
print(mat[0,0])
#slicing of matrix => only 0th column
print(mat[:,0])
#slicing of matrix => only 0th row
print(mat[0,:])
#slicing of matrix => of a specific rows and columns
print(mat[0:3,0:3]) #first 3 row and 3 column

##maskig a matrix
#values > 50
print(mat>50) 
print(mat[mat>50])

##np.zeros(ndimensions) => creates n x m zero matrics
numzero = np.zeros(4);
numzero2x2 = np.zeros((2,2));
print(numzero2x2)

##np.ones(ndimensions) => creates n x m one matrics
numone = np.ones(4);
numone2x2 = np.ones((2,2));
print(numone2x2)

##dot multiplication of 1d array: arr1 and arr2
#process1: using for loop and list
result = 0
for i in range(len(arr1)):
   result = result + (arr1[i]*arr2[i])
print(result)

#process2: using zip
result = 0
for x1,x2 in zip(arr1,arr2):
   result = result + (x1*x2)
print(result)

#process3: np.dot(mat1,mat2)
result = np.dot(arr1,arr2)
print(result)

##mutrix multiplication of n * 1 dimension
climate_data = [[73,67,43],
                [91,88,64],
                [87,134,58],
                [102,43,37],
                [69,96,70]]
weight = [0.3,0.2,0.5]
result = np.matmul(climate_data,weight)
print(result)
