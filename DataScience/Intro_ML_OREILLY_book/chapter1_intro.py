import numpy as np
import pandas as pd
import scipy.sparse as sprs
import matplotlib.pyplot as plt

def main():
    ###numpy
    #print('main funciton')
    #x = np.array([[1,2,3],[4,5,6]])
    #print('x: \n{}'.format(x))
    
    ##identity matrix 4x4
    #eye = np.eye(4)
    #print('eye = \n{}'.format(eye))
    
    ###scipy sparse
    ##index wise representation method-1
    #sparse_matrix = sprs.csr_matrix(eye)
    #print('SciPy sparse CSR Matrix: \n{}'.format(sparse_matrix))

    ##index wise representation method-2
    #data = np.ones(4) #[1. 1. 1. 1.]
    #row_indices = np.arange(4) #[0,1,2,3]
    #col_indices = np.arange(4) #[0,1,2,3]

    ##coo means co-ordinate
    #eye_coo = sprs.coo_matrix((data,(row_indices,col_indices))) #((ones,(row,col)))
    #print('SciPy Sparse CSR matrix \n{}'.format(eye_coo))

    ####matplotlib.pyplot
    #x = np.linspace(-10,10,100) #(start,stop,steps)
    #y = np.sin(x)
    ##the plot function makes a line chart of one array against another
    #plt.plot(x, y, marker = "x")
    #plt.show()

    ###pandas
    #create a dictionary for making a dataset of people
    data = {'NAME': ['John','Anna','Peter','Linda'],
            'LOCATION':['New York','Paris','Berlin','London'],
            'AGE':[24,13,53,33]
            }

    #converting dictionary to Dataframe
    data_pandas = pd.DataFrame(data)
    print('PEOPLE TABLE\n{:}'.format(data_pandas))

    #query from the dataframe
    print(data_pandas[data_pandas.AGE>30])
    print(data_pandas[data_pandas['AGE']>30])




if __name__ == '__main__':
    main()