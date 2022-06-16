import csv
import numpy as np 
import matplotlib.pyplot as plt

class Visualization():
    
    def __init__(self):
        res = open('results/csv/results.csv', 'r')
        self.results = csv.DictReader(res, delimiter= ',')
        excludedMetrics = [elem for elem in self.results.fieldnames if elem != 'model' and elem != 'test_index' and elem != 'train_index']
        self.metrics = [x for x in self.results.fieldnames if x in excludedMetrics]
    
    def returnResultsDict(self):
        return self.results

    def allVisualizations(self, saveFig = bool):
        print("---------- Generating plots for each metric found in results.csv")
        x = []
        y = []
        for row in self.results: 
            print("Results of model below: ")
            print("----------")
            for i in self.metrics:
                x.append(row['Epoch'])
                y.append(row[i])
                print(i, row[i])
                if saveFig == True:
                    plt.bar(x, y, width = 0.72, label = i)
                    plt.xlabel('Epoch')
                    plt.title('{} plot'.format(i))
                    plt.savefig('results/figs/%s plot.png'%(i))
    
    def selectVisualization(self, metric, saveFig = bool):
        print(metric)
        x = []
        y = []
        for row in self.results:
            x.append(row['Epoch'])
            y.append(row[metric])
            print(row['Epoch'], row[metric])
            if saveFig == True:
                plt.bar(x, y, width = 0.72, label = metric)
                plt.xlabel('Epoch')
                plt.ylabel(metric)
                plt.title('{} plot'.format(metric))
                plt.savefig('results/figs/%d plot.png'%(metric))
        