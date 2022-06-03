from sklearn.metrics import *

from data import Data
from model import Models

class fitModel():
    
    def __init__(self, model, data):
        self.model = model
        self.data = data
        
    def fit(self):
        ret = {}
        M, L, kf = self.data
        model = self.model
        for ids, (train_index, test_index) in enumerate(kf.split(M, L)):
            model.fit(M[train_index], L[train_index])
            pred = model.predict(M[test_index])
            ret[ids]= {'clf': model
                    ,'train_index': train_index
                    ,'test_index': test_index
                    ,'accuracy': accuracy_score(L[test_index], pred)
                    , 'balanced_accuracy': balanced_accuracy_score(L[test_index], pred)
                    , 'precision': precision_score(L[test_index], pred)
                    ,'average_precision': average_precision_score(L[test_index], pred)
                    , 'roc_auc': roc_auc_score(L[test_index], pred)
                    }
        return ret
   
    
        