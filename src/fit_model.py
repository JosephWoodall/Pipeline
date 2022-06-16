import os
import csv

from sklearn.metrics import *
from sklearn.model_selection import GridSearchCV, KFold

from src.toyData import toyData
from src.model import Models

class fitModel():
    """class to fit the data from Data.finalData() to the model from Model.finalModel()
    """
    
    def __init__(self, model, data):
        self.model = model
        self.data = data
        self.param_grid = {}
        if self.model == 'RandomForestClassifier_':
            self.param_grid = {
                'max_features': ['auto', 'sqrt', 'log2']
                , 'criterion': ['gini', 'entropy']
            }
        
    def fit(self, parameters = bool, hyperParameterTunedModel = bool):
        """main function to fit the data from the __init__ above.

        Returns:
            ret: nested dictionary of results from the fit.
            results.csv: csv that hosts the results from fit().
        """
        ret = {}
        M, L, kf = self.data
        model = self.model
        for ids, (train_index, test_index) in enumerate(kf.split(M, L)):
            if hyperParameterTunedModel == True:
                kf_inner = KFold(n_splits = 3, shuffle = True)
                search = GridSearchCV(model, param_grid=self.param_grid, scoring = 'accuracy', cv = kf_inner, refit = True)
                result = search.fit(M[train_index], L[train_index])
                best_model = result.best_estimator_
                pred = best_model.predict(M[test_index])
                ret[ids]= {'model': best_model
                        ,'train_index': train_index
                        ,'test_index': test_index
                        ,'accuracy': accuracy_score(L[test_index], pred)
                        , 'balanced_accuracy': balanced_accuracy_score(L[test_index], pred)
                        , 'precision': precision_score(L[test_index], pred)
                        ,'average_precision': average_precision_score(L[test_index], pred)
                        , 'roc_auc': roc_auc_score(L[test_index], pred)
                        }
            else:
                model.fit(M[train_index], L[train_index])
                pred = model.predict(M[test_index])
                ret[ids]= {'model': model
                        ,'train_index': train_index
                        ,'test_index': test_index
                        ,'accuracy': accuracy_score(L[test_index], pred)
                        , 'balanced_accuracy': balanced_accuracy_score(L[test_index], pred)
                        , 'precision': precision_score(L[test_index], pred)
                        ,'average_precision': average_precision_score(L[test_index], pred)
                        , 'roc_auc': roc_auc_score(L[test_index], pred)
                        }
            header = sorted(set(i for b in map(dict.keys, ret.values()) for i in b))
            with open('results/csv/results.csv', 'w', newline="") as f:
                write = csv.writer(f)
                write.writerow(['Epoch', *header])
                for a, b in ret.items():
                    write.writerow([a]+[b.get(i, '') for i in header])
            header_exclude = [elem for elem in header if elem != 'model' and elem != 'test_index' and elem != 'train_index']
        print("---------- Model successfully fit! Results from model are saved in results/csv/results.csv! ----------")
        print("---------- Available metrics: {} ----------".format(header_exclude))
        if parameters == True: 
            model.get_params(deep = True)
        #return ret
    
    
    
        