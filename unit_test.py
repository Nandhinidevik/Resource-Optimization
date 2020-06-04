import unittest
class test_optimization(unittest.TestCase):
    #to check the proper output for a proper input
    def testoptimization(self):
        result = optimize("1150 units for 1 hour")
        print(result)
        ExpectedOutput = {'Output': [{'region': 'New York', 'total_cost': '$10150', 'machines': [('XLarge', 1), ('Large', 1)]}, {'region': 'India', 'total_cost': '$9520', 'machines': [('8XLarge', 7), ('Large', 3)]}, {'region': 'China', 'total_cost': '$8570', 'machines': [('XLarge', 1), ('Large', 1)]}]}                                                                                                                                     
        print(ExpectedOutput)
        self.assertEqual(result, ExpectedOutput)
    #to check the error message when incorrect input is given
    def testincorrectinput(self):
        result = optimize("1150")
        print(result)
        ExpectedOutput = "Incorrect Input format"                                                
        print(ExpectedOutput)
        self.assertEqual(result, ExpectedOutput)
    #to check the error message when units given is not a multiple of 10
    def testincorrectunits(self):
        result = optimize("5 units for 1 hour")
        print(result)
        ExpectedOutput = "Units should be multiple of 10 and the time in hour should be proper"                                                
        print(ExpectedOutput)
        self.assertEqual(result, ExpectedOutput)
    #to check the error message when time given is incorrect
    def testincorrecthour(self):
        result = optimize("50 units for -1 hour")
        print(result)
        ExpectedOutput = "Units should be multiple of 10 and the time in hour should be proper"                                                
        print(ExpectedOutput)
        self.assertEqual(result, ExpectedOutput)
        
if __name__== '__main__':
    unittest.main()
