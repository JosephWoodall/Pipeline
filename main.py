from src.fit_model import fitModel
from src.visualization import Visualization
from src.toyData import toyData
from src.model import Models

toyData1 = toyData(100, 100 , 10).generateToyData(preProcessing=True)
#financialData = Data(100, 100, 10).generateToyFinancialData()
model = Models().finalModel('RandomForestClassifier_')
fit = fitModel(model, toyData1).fit(parameters = True, hyperParameterTunedModel=True)
#print(fit)
#plots = Visualization().allVisualizations(saveFig = False)
