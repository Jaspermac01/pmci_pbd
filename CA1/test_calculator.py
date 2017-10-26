
from calculator import Calculator

import unittest

class TestCalculator(unittest.TestCase):

# test 1
    def test_calculator_add(self):
        result = Calculator().add(5.0,5)
        self.assertEqual(10.0, result)
        result = Calculator().add(2.0,3)
        self.assertEqual(5.0, result)
        
# test 2        
    def test_calculator_sub(self):
        result = Calculator().subtract(5,5)
        self.assertEqual(0, result)
        result = Calculator().subtract(3,2)
        self.assertEqual(1, result)
        
# test 3           
    def test_calculator_multiply(self):
        result = Calculator().multiply(5,5)
        self.assertEqual(25.0, result)        
        result = Calculator().multiply(5,1)
        self.assertEqual(5.0, result) 
        result = Calculator().multiply(5,1)
        self.assertEqual(5.0, result) 
        result = Calculator().multiply(5, 0.2)
        self.assertEqual(1.0, result) 

# test 4        
    def test_calculator_divide(self):
        result = Calculator().divide(5.0,5)
        self.assertEqual(1.0, result)        
        result = Calculator().divide(5.0,1)
        self.assertEqual(5.0, result) 
        result = Calculator().divide(1.0,5)
        self.assertEqual(0.2, result) 
        result = Calculator().divide(5.0, 0.2)
        self.assertEqual(25.0, result)      

# test 5        
    def test_calculator_exponential(self):
        result = Calculator().exponent(5.0,2)
        self.assertEqual(25.0, result)        
        result = Calculator().exponent(5.0,3)
        self.assertEqual(125.0, result)        

# test 6             
    def test_calculator_square(self):
        result = Calculator().square(5.0)
        self.assertEqual(25.0, result)        
        result = Calculator().square(7)
        self.assertEqual(49.0, result)  

# test 7             
    def test_calculator_cube(self):
        result = Calculator().cube(5.0)
        self.assertEqual(125.0, result)        
        result = Calculator().cube(7)
        self.assertEqual(343.0, result)  
 
# test 8             
    def test_calculator_sin(self):
        result = Calculator().sin(3)
        self.assertEqual(0.1411200080598672, result)        
        result = Calculator().sin(-3)
        self.assertEqual(-0.1411200080598672, result)  
        
# test 9             
    def test_calculator_cos(self):
        result = Calculator().cos(3)
        self.assertEqual(-0.9899924966004454, result)        
        result = Calculator().cos(-3)
        self.assertEqual(-0.9899924966004454, result)  
        result = Calculator().cos(0)
        self.assertEqual(1.0, result)         
        
# test 10             
    def test_calculator_tan(self):
        result = Calculator().tan(3)
        self.assertEqual(-0.1425465430742778, result)        
        result = Calculator().tan(-3)
        self.assertEqual(0.1425465430742778, result)
        result = Calculator().tan(0)
        self.assertEqual(0.0, result)           
                
if __name__ == '__main__':
    unittest.main()



