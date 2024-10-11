###https://blog.enterprisedna.co/pandas-drop-index/
###PANDAS is directly build of NUMPY
###akhon akta jinish shikhbo seta holo: pandas er data frame
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
# ##jaha data frame tahai table
# #SYNTEX1 : dataFrame_Name = pd.DataFrame(data = [numerical or categorical], columns = ['Column_Name'])
# #SYNTEX2 : dataFrame_Name = pd.DataFrame({'Column_Name1': [values], 'Column_Name2': [values]})

# #creating dataFrame
# populationData = pd.DataFrame(data = [2,4,7,9], columns = ['People'])

# #creating dataFrame
# populationData1 = pd.DataFrame({'Time': [7.12,8,9,10]})

# #printing dataframe
# print(populationData)

# #printing dataframe
# print(populationData1)

# #joining the two dataframe into one data frame
# MarketData = populationData.join(populationData1)

# #printing the dataframe
# print(MarketData)

# #renaming a column of a dataframe
# MarketData = MarketData.rename(index={0: 'Saturday', 1: 'Sunday', 2: 'Monday', 3: ' Tuesday'}) 

# #maping the values of a column
# MarketData['Time'] = MarketData['Time'].map({7: 'Very Early', 8: 'Early', 9: 'Late' ,10: 'Very Late'}) 

# #printing the dataframe
# print(MarketData)

# #converting the dataframe into excel and save it to local storage
# #SYNTEX : dataframe_name.to_excel('file_name.xlsx',sheet_name='sheet_name')
# #MarketData.to_excel('./Drawable/MarketData.xlsx',sheet_name='sheet1')

# ##Akhon dekhbo kivabe dataframe k customize kora jay
# #show only all the columns
# pd.set_option('display.max_columns', None)
# print(MarketData)

# #column resetting as user defined '1'
# pd.set_option('display.max_columns', 1)
# print(MarketData)

# #reset the default 
# pd.reset_option('display.max_columns')
# print(MarketData)

# #column-width resetting
# pd.set_option('max_colwidth', 10)
# print(MarketData)

# #precision resetting of the dataframe user defined '2'
# pd.set_option('display.precision', 1)
# print(MarketData)

# #show only all the rows
# pd.set_option('display.max_rows', None)
# print(MarketData)

# #row resetting as user defined '2'
# pd.set_option('display.max_rows', 2)
# print(MarketData)

# #reset the default 
# pd.reset_option('display.max_rows')
# print(MarketData)

# #prints first five rows of the dataset
# print("first five rows of the dataset")
# print(MarketData.head())

# #prints first 2 rows of the dataset
# print("first two rows of the dataset")
# print(MarketData.head(2))

###Read From CSV File
dataset= pd.read_csv('Drawable/DataSet.csv')

##Displaying the data
print(dataset)
#Single Column "Name"
print(dataset['Name'])
#Two Column "Name" "Age"
print(dataset[['Name','Age']])

##Analyzing Data
#maximum age
print(dataset['Age'].max())

#Statistical Summary of the Numerical Data only (Categorical data are skipped by default)
print(dataset.describe())

#Filtering data
print(dataset[dataset['Age']>12])

#converting dataframe to datamatrix [We recommend using DataFrame.to_numpy() instead]
data_matrix = dataset.values
print(data_matrix)


# X=dataset.iloc[:,1:2].values
# print(X)

# dataset.plot()
# plt.show()

# s=pd.Series([1,2,3,"f"])
# date=pd.date_range('20200829',periods=6)
# print(date)

# df=pd.DataFrame(np.random.randn(6,4),index=date,columns=list('ABCD'))
# print(df)

# df['E']=['One','Two','Three','Four','Five','Six']
# print(df)

# s1=pd.Series([1,2,3,4,5,6],index=pd.date_range('20200904', periods=6))
# print(s1)

# df['F']=s1
# print(df)

# df.to_excel('./Drawable/dateSet.xlsx',sheet_name='sheet1')
# df1=pd.read_excel('./Drawable/dateSet.xlsx',sheet_name='sheet1',index_col=None,na_values=['Na'])
# print(df1)

# #df=df.cumsum()
# df.plot()
# plt.show()

# pd.set_option('display.max_columns', None) 
# climate_test_dataset = pd.read_csv('./Drawable/DailyDelhiClimateTest.csv')
# print(climate_test_dataset)
# climate_train_dataset = pd.read_csv('./Drawable/DailyDelhiClimateTrain.csv',index_col=False,header=None)
# print(climate_train_dataset)
# #climate_dataset.drop(columns='',axis=1,inplace=True)
# #climate_dataset = climate_dataset.to_csv(header=None, index= False)
# climate_train_dataset.iloc[1: , 2:]
# print(climate_train_dataset.iloc[1: , 3:])
