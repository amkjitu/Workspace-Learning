'''
Ghotona
-------
Let's assume that a hobby botanist is interested in distinguishing the species of some iris flowers that
she has found.She collected some measurements associate with each iris: the length and width of the petals
and the length and width of the sepals, all measured in cm.
She also has the measurements of some iris that have been previously identified by an expert botanist as 
belonging to the species setosa, vericolor or virginica.
For these measurements, she can be certain of which species eash iris belongs to.

Goal
----
Build a machine learning model that can learn from the measurements of those irises whose species is known, 
so that we can predict the species for a new iris.
'''

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import mglearn
from sklearn.neighbors import KNeighborsClassifier

def main():
    iris_dataset = load_iris()
    print(type(iris_dataset))
    print(iris_dataset.keys())
    print(iris_dataset['DESCR'][:193]) #short description of the data set
    #print('Target names: {}'.format(iris_dataset['target_names'])) #species of the flower that we want to predict
    #print('Feature names: {}'.format(iris_dataset['feature_names'])) #species of the flower that we want to predict
    #print('Shape of data: {}'.format(iris_dataset['data'].shape)) #rows 150 col 4: 4 features of flowers with 150 samples
    #print('First 5 col of the data: \n{}'.format(iris_dataset['data'][:5])) #rows 150 col 4: 4 features(sepal width,sepal height,petal width,petal height) of flowers with 150 samples
    #print('Shape of the target: \n{}'.format(iris_dataset['target'].shape)) #shape of the target
    #print('Target: \n{}'.format(iris_dataset['target'])) # 150 samples targets to 0,1 or 3. 0 means setosa, 1 means versiclolor, 2 means virginica
    
    #splitting the data into training dataset and testing dataset to the ratio of 75:25
    X_train,X_test,y_train,y_test=train_test_split(iris_dataset['data'],iris_dataset['target'],random_state=0)
    #print('X_train shape: {}'.format(X_train.shape))
    #print('X_train shape: {}'.format(y_train.shape))
    #print('X_train shape: {}'.format(X_test.shape))
    #print('X_train shape: {}'.format(y_test.shape))

    iris_train_dataframe = (pd.DataFrame(X_train,columns = iris_dataset.feature_names))
    #print(iris_train_dataframe)

    #grr = pd.plotting.scatter_matrix(iris_train_dataframe,c=y_train,figsize=(15,15),marker = 'o',hist_kwds = {'bins': 20}, s = 50, alpha = 0.8, cmap = mglearn.cm3 )

    #how data are scattered
    #plt.show()

    #Model training: fitting the training data set
    knn = KNeighborsClassifier(n_neighbors = 1)
    knn.fit(X_train,y_train)

    #Model prediction:
    y_pre = knn.predict(X_test)

    print('test sets: \n{}'.format(X_test))
    print('Test set prediction {}'.format(y_pre))
    print('Predicted Species: {}'.format(iris_dataset['target_names'][y_pre]))

    #Model Accquracy:
    print('Accuracy = {:.2f}'.format(np.mean(y_pre==y_test)))
    #print('Accuracy = {}'.format(knn.score(X_test,y_test)))

    #now using the predicted model I will test my own
    my_X_test = [[0.1,0.3,0.4,0.5]] #sepal width,sepal height,petal width,petal height
    my_y_pre = knn.predict(my_X_test)

    print('My test predict {}'.format(my_y_pre))
    print('My test predicted species {}'.format(iris_dataset['target_names'][my_y_pre]))
    print('Accuracy = {}'.format(knn.score(my_X_test,my_y_pre)))



if __name__ =='__main__':
    main()

