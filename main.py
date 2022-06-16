from src.fit_model import fitModel
from src.visualization import Visualization
from src.toyData import toyData
from src.model import Models

toyData = toyData(100, 100 , 10).generateToyData(preProcessing=True, label = None)
#financialData = Data(100, 100, 10).generateToyFinancialData()
model = Models().finalModel('RandomForestClassifier_')
fit = fitModel(model, toyData).fit(parameters = True)
print(fit)
plots = Visualization().allVisualizations(saveFig = True)
