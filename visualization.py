import numpy as np 

class Visualization():
    
    def __init__(self):
        self.results = np.genfromtxt('data/results.csv', delimiter = ',')

    """ for each key in fitModel.fit() -> ret after position 2, plot key:value """
    
    """
    def accuracy()....
    """
    
    """
    def balanced_accuracy()...
    """
    
    """
    .....etc.....
    """

    

"""
# Pseudo code below:
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
#
#
"""    
