"""Classification Pipeline

Returns:
    Final Analytics of Selected Classification Algorithm: 
    
    Available Models for use include: Random Forest Classifier, Logistic Regression, and Decision Tree Classifier
    Available Metrics for result interpretation include: accuracy, balanced accuracy, precision, average percision, and roc auc.
"""
import matplotlib.pyplot as plt
from sklearn.metrics import *
from data import Data
from fit_model import fitModel
from model import Models

data = Data(100,100,10).finalData()
print(data)    
listOfModels = Models().listOfModels()
print(listOfModels)
model = Models().finalModel()
fit = fitModel(model, data).fit()
print(fit)
 



#class Pipeline:   

#
#    
#    def error_metrics():
#        
#        """
#        Which are useful?
#        calculate handful to be covered in most scenarios
#        
#        this is covered in fit_model()
#        """
#        pass
#        
#
#    def visualization(metric):
#        """
#        everyone loves pictures
#        roc curve
#        predictions vs actual
#        confusion matrices? Multiclass covered?
#        distribution of error metrics
#        """        
#        res = Pipeline.fit_model()
#        
#        metric = input
#        
#        
#        
#        if metric == "accuracy":
#            temp = metric
#            res_keys = [key for key, val in res.items() if temp in val]
#            res_values = [val[temp] for key, val in res.items() if temp in val]
#            print(list(sorted(res_keys)))
#            print(list(sorted(res_values)))
#            #roc_auc = {res_keys[i]: res_values[i] for i in range(len(res_keys))}
#            plt.plot(res_keys, res_values)
#            plt.title(temp + " plot")
#            plt.show()
#        
#        if metric == "balanced_accuracy":
#            temp = metric
#            res_keys = [key for key, val in res.items() if temp in val]
#            res_values = [val[temp] for key, val in res.items() if temp in val]
#            print(list(sorted(res_keys)))
#            print(list(sorted(res_values)))
#            #roc_auc = {res_keys[i]: res_values[i] for i in range(len(res_keys))}
#            plt.plot(res_keys, res_values)
#            plt.title(temp + " plot")
#            plt.show()
#        
#        if metric == "precision":
#            temp = metric
#            res_keys = [key for key, val in res.items() if temp in val]
#            res_values = [val[temp] for key, val in res.items() if temp in val]
#            print(list(sorted(res_keys)))
#            print(list(sorted(res_values)))
#            #roc_auc = {res_keys[i]: res_values[i] for i in range(len(res_keys))}
#            plt.plot(res_keys, res_values)
#            plt.title(temp + " plot")
#            plt.show()
#            
#        if metric == "average_precision":
#            temp = metric
#            res_keys = [key for key, val in res.items() if temp in val]
#            res_values = [val[temp] for key, val in res.items() if temp in val]
#            print(list(sorted(res_keys)))
#            print(list(sorted(res_values)))
#            #roc_auc = {res_keys[i]: res_values[i] for i in range(len(res_keys))}
#            plt.plot(res_keys, res_values)
#            plt.title(temp + " plot")
#            plt.show()
#            
#        if metric == "roc_auc":
#            temp = metric
#            res_keys = [key for key, val in res.items() if temp in val]
#            res_values = [val[temp] for key, val in res.items() if temp in val]
#            print(list(sorted(res_keys)))
#            print(list(sorted(res_values)))
#            #roc_auc = {res_keys[i]: res_values[i] for i in range(len(res_keys))}
#            plt.plot(res_keys, res_values)
#            plt.title(temp + " plot")
#            plt.show()
#
#        
#
#    def results():
#        """
#        handy dandy results csv 
#        return which models ran and their results
#        visualizations again
#        """
#        pass
#    
#    def debug():
#        M, L, kf = Pipeline.pre_processing()
#        print("M shape: {}".format(M.shape))
#        print("L shape {}".format(L.shape))
#        print(kf)
#
#"""#