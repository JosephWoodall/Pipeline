from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

class Models():
    """Hosts the models used for fitModel()
    """

    def __init__(self):
        self.algo = {
            
            # Classifiers #
            "RandomForestClassifier_":RandomForestClassifier(), 
            "LogisticRegression_":LogisticRegression(),
            "DecisionTreeClassifier_":DecisionTreeClassifier()
            
            # Regressors #
            
        }

    
    def listOfModels(self): #helper function
        listOfAlgos = list(self.algo) #print the algo dict for user to see what is available
        print("Available algorithms: {}".format(listOfAlgos))
        
    def finalModel(self):  
        self.choice = input("Which model would you like to use?: ")
        if self.choice in self.algo:
            return self.algo.get(self.choice)
    


