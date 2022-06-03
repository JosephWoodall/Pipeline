import numpy as np
from sklearn.model_selection import KFold 

class Data(object):
    """class which ingests the data for downstream use 

    Args:
        parameter (row): number of rows for generateToyData()
        parameter (col): number of columns for generateToyData()
        parameter(n_folds): number of folds for k-fold cross validator variable. Must be at least 2
    """
    
    def __init__(self, row, col, n_folds):
        self.row = row 
        self.col = col 
        self.n_folds = n_folds
        
    
    def generateToyData(self):
        """Toy data for testing purposes only

        Returns:
            array: random data using row and col as user input
        """
        M = np.random.rand(self.row, self.col)
        L = np.random.rand(M.shape[0])
        L = np.rint(L)
        data = (M, L, self.n_folds)
        return data
    
    def preProcessing(self):
        """Preprocesses passed data if needed

        Returns:
            constant M: ndarray of dtype float64
            constant L: ndarray with shape of M[0]
            variable kf: K-Fold Cross Validator
        """
        data = Data(self.row, self.col, self.n_folds).generateToyData()
        M, L, n_folds = data
        M = M 
        L = L 
        kf = KFold(n_splits = self.n_folds)
        return M, L, kf
    
    def finalData(self):
        """Final output of data for later use

        Returns:
            output of preProcessing: same as output of preProcesing()
        """
        M, L, kf = Data(self.row, self.col, self.n_folds).preProcessing()
        return M, L, kf        
        