import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import f_regression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#importing table from local storage
UniversityData = pd.read_csv("C:/Users/HP 840 G1/Documents/VS Code Projects/Workspace Learning/DataScience/DataScienceInPython/Drawable/1.Simple_linear_regression.csv")
print("Table of SAT and GPA")
print(UniversityData)

#Spliting Training and Testing
#train_test_split(Column, test_size  = 0-1, random_state = n, shuffle = True/False) default "shuffle = True"
#Here, column : the column of the dataset which i want to spilt
#        test_size : 0.2 means 20% of the data will be split for test and rest of the 1-0.2 = 0.8 infact 80% for training
#        random_state : 42 means in each excution jate aki vabe (42) constant ei thake shuffle ta
# NOTE: "shuffle = False" kora thakle random_state() kora akta obokash matro

SAT_List = UniversityData['SAT'].to_list()
print("SAT: ")
print(SAT_List)
training_data_SAT,testing_data_SAT =  train_test_split(SAT_List, test_size = 0.3, random_state = 42)

print("Training SAT:")
print(training_data_SAT)

print("Testing SAT:")
print(testing_data_SAT)

GPA_List = UniversityData['GPA'].to_list()
print("GPA: ")
print(GPA_List)
training_data_GPA,testing_data_GPA =  train_test_split(GPA_List, test_size = 0.3, random_state = 42)

print("Training GPA:")
print(training_data_GPA)

print("Testing GPA:")
print(testing_data_GPA)

UniversityData_Traning = pd.DataFrame({'SAT': training_data_SAT, 'GPA': training_data_GPA})
print("TRAINING Dataset of SAT and GPA")
print(UniversityData_Traning)

print("TRAINING Dataset of SAT and GPA")
UniversityData_Testing = pd.DataFrame({'SAT': testing_data_SAT, 'GPA': testing_data_GPA})
print(UniversityData_Testing)

##Akhon ai traing dataset theke regression korbo and dekhbo seta testing data set er sathe kotota reliable
LRegre = LinearRegression()

x = UniversityData_Traning['SAT']
x = x.values.reshape(-1,1)
y = UniversityData_Traning['GPA']

LRegre.fit(x,y)

b0 = (LRegre.intercept_).round(3)
print(type(b0))

b1 = np.float64(LRegre.coef_)
print(type(b1))

b1 = (b1).round(3)
print("The Equation of the simple linear regression: y = ",b0," + ", b1,"x")

