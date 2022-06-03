import os
import csv

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
            header = sorted(set(i for b in map(dict.keys, ret.values()) for i in b))
            with open('data/results.csv', 'w', newline="") as f:
                write = csv.writer(f)
                write.writerow(['location', *header])
                for a, b in ret.items():
                    write.writerow([a]+[b.get(i, '') for i in header])
        return ret
   
    
        