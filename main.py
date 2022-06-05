from data import Data
from fit_model import fitModel
from model import Models

import matplotlib.pyplot as plt 

# Main run portion for now
data = Data(100,100,10).finalData()
print(data)  
#preprocessing = Data(100, 100, 10).preProcessing()
#print(preprocessing)
listOfModels = Models().listOfModels()
print(listOfModels)
model = Models().finalModel()
fit = fitModel(model, data).fit()
print(fit)