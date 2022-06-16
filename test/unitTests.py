import unittest

class unitTests(unittest.TestCase):
    
    def testMain(self):
        print("---------- Main")

    def testToyData(self):
        print("---------- testToyData")
        
    def testRawData(self):
        print("---------- testRawData")
    
    def testModel(self):
        print("---------- testModel")
    
    def testFitModel(self):
        print("---------- testFitModel")

    def testVisualizations(self):
        print("---------- testVisualizations")
    
    def testConfig(self):
        print("---------- testConfig")
    
    def testConnection(self):
        print("---------- testConnection")
    
    def testLogs(self):
        print("---------- testLogs")
    
if __name__ == '__main__':
    unittest.main()