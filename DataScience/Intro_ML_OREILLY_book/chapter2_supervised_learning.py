import numpy as np
import pandas as pd
import mglearn
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

def working_with_dataframe():

    customer_dataset = {
                        'Age':[66,52,22,25,44,39,26,40,53,64,58,33],
                        'Number of cars owned':[1,2,0,1,0,1,1,3,2,2,2,1],
                        'Owns house':['yes','yes','no','no','no','yes','no','yes','yes','yes','yes','no'],
                        'Numbers of children':[2,3,0,1,2,2,2,1,2,3,2,1],
                        'Marital status':['widowed','married','married','single','divorced','married','single','married','divorced','divorced','married','single'],
                        'Owns a dog':['no','no','yes','no','yes','yes','no','yes','no','no','yes','no'],
                        'Bought a boat':['yes','yes','no','no','no','no','no','no','yes','no','yes','no']
                        }

    df_customer_dataset = pd.DataFrame(customer_dataset)
    print(df_customer_dataset)
    df_customer_dataset.columns = df_customer_dataset.columns.str.replace(' ','_')
    print(df_customer_dataset)

    np_array_customer_dataset = df_customer_dataset.to_numpy()

    print(df_customer_dataset[df_customer_dataset[df_customer_dataset.columns[6]]=='yes'])
    print(df_customer_dataset.columns[6])
    #print(np_array_customer_dataset)

def Dataset_two_class_classification():
    X,y = mglearn.datasets.make_forge()
    mglearn.discrete_scatter(X[:,0],X[:,1],y)
    print('X shape : {}'.format(X.shape))
    print(X)
    plt.legend(["Class 0","Class 1"],loc=4)
    plt.xlabel('First feature')
    plt.ylabel('Second feature')
    #plt.show()
    

def Dataset_regression():
    X,y = mglearn.datasets.make_wave(n_samples=40)
    print('X shape : {}'.format(X.shape))
    print(X)
    plt.plot(X,y,'o')
    plt.ylim(-3,3)
    plt.xlabel('Feature')
    plt.ylabel('Target')
    plt.show()
    
def brest_cancer_prediction_knn_classifier():
    ####ei function e 2 ta part: 1.optional practice, 2.main code 
    #records clinical measurements of breast cancer tumors. Each tumor
    #is labeled as 'benign' (for harmless tumors) or 'malignant' (for cancerous tumors),
    #TASK is to learn to predict whether a tumor is malignant based on the measurements of the tissue.
    cancer = load_breast_cancer()

    ###1.ekhane kichu learn and practice korsi
    #b = [1,2,3,2,2,2,2,2,3,3,3,1]
    #print(np.bincount(b)) # [0,2,6,4] means 0 ache 0 ta, 1 ache 2 ta, 2 ache 6 ta, 3 ache 4 ta

    #Of these 569 data points, 212 are labeled as malignant and 357 as benign:
    #counto = 0
    #countl = 0
    #for i in cancer.target:
    #    if i==0:
    #        counto=counto+1
    #    else : countl = countl +1
    #print('benign: {}, malignant: {}'.format(countl,counto))

    ##Of these 569 data points, 212 are labeled as malignant and 357 as benign:
    #print({n: v for n, v in zip(cancer.target_names, np.bincount(cancer.target))})
    #tnames,tcount = zip(cancer.target_names, np.bincount(cancer.target))
    #print(tnames,tcount)

    ##k er man er opor depend kore graph
    #mglearn.plots.plot_knn_classification(n_neighbors=3)
    #plt.show()

    ###2.we evaluate training and test set performance with different numbers of neighbors with the realworld data.
    X_train,X_test,y_train,y_test = train_test_split(cancer.data,cancer.target,stratify=cancer.target,random_state=66)
    training_accuracy = []
    text_accuracy = []
    #try n_neighbors from 1 to 10
    neighbors_settings = range(1,11)
    for n_neighbors in neighbors_settings:
        #build the model
        clf = KNeighborsClassifier(n_neighbors = n_neighbors)
        clf.fit(X_train,y_train)
        #record training set accuracy
        training_accuracy.append(clf.score(X_train,y_train))#record training set accuracy
        #record generalization accuracy
        text_accuracy.append(clf.score(X_test,y_test))

    plt.plot(neighbors_settings,training_accuracy,label="training accuracy")
    plt.plot(neighbors_settings,text_accuracy,label="test accuracy")
    plt.ylabel("Accuracy")
    plt.xlabel("n_neighbors")
    plt.legend()
    plt.show()


def analyzing_kNeighbors_classifier():
    X,y = mglearn.datasets.make_forge()
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    clf = KNeighborsClassifier(n_neighbors = 3)
    clf.fit(X_train,y_train)

    print('Test-set predictions: {}'.format(clf.predict(X_test)))
    print('Test-set accuracy: {:.2f}'.format(clf.score(X_test,y_test)))

    fig, axes = plt.subplots(1, 3, figsize=(10, 3))
    for n_neighbors, ax in zip([1, 3, 9], axes):
        # the fit method returns the object self, so we can instantiate
        # and fit in one line
        #clf = KNeighborsClassifier(n_neighbors=n_neighbors).fit(X, y)
        clf = KNeighborsClassifier(n_neighbors=n_neighbors).fit(X_train, y_train)
        accuracy = clf.score(X_test,y_test)
        mglearn.plots.plot_2d_separator(clf, X, fill=True, eps=0.5, ax=ax, alpha=.4)
        mglearn.discrete_scatter(X[:, 0], X[:, 1], y, ax=ax)
        ax.set_title("{} neighbor(s) accuracy {:.2f}".format(n_neighbors,accuracy*100))
        ax.set_xlabel("feature 0")
        ax.set_ylabel("feature 1")
    axes[0].legend(loc=3)
    axes[1].legend(loc=3)
    axes[2].legend(loc=3)
    plt.show()


def main():
    #working_with_dataframe()
    #Dataset_two_class_classification()
    #Dataset_regression()
    #analyzing_kNeighbors_classifier()
    brest_cancer_prediction_knn_classifier()



if __name__ == '__main__':
    main()



