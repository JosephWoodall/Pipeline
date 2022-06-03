from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

class Models():

    def __init__(self):
        self.algo = {
            "RandomForestClassifier_":RandomForestClassifier(), 
            "LogisticRegression_":LogisticRegression()
        }

    
    def listOfModels(self): #helper function
        listOfAlgos = list(self.algo) #print the algo dict for user to see what is available
        print("Available algorithms: {}".format(listOfAlgos))
        
    def finalModel(self):  
        self.choice = input("Which model would you like to use?: ")
        if self.choice in self.algo:
            return self.algo.get(self.choice)
    


