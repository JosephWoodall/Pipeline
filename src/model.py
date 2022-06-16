from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

class Models():
    """Hosts the models used for fitModel()
    """

    def __init__(self):
        self.algo = {
            
            # Classifiers #
            "RandomForestClassifier_":RandomForestClassifier(), 
            "LogisticRegression_":LogisticRegression(),
            "DecisionTreeClassifier_":DecisionTreeClassifier(), 
            "SupportVectorMachine_": SVC()
            
            # Regressors #
            
        }

    
    def listOfModels(self): #helper function
        listOfAlgos = list(self.algo) #print the algo dict for user to see what is available
        print("Available algorithms: {}".format(listOfAlgos))
        
    def finalModel(self, model):  
        #self.model = input("Which model would you like to use?: ")
        if model in self.algo:
            return self.algo.get(model)
    


