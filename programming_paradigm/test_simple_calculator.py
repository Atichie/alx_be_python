import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

        def setup(self):
            self.calc = SimpleCalculator()

        def test_addition(self):
            self.assertEqual(self.calc.add(2, 3), 5)

        def test_subtraction(self):
            self.assertEqual(self.calc.subtract(5, 3), 2)

        def test_multiplication(self):
            self.assertEqual(self.calc.multiply(5, 3), 15)

        def test_division(self):
            self.assertEqual(self.calc.divide(8, 2), 4)
            
    

name = "_main_"
if name == "_main_":
    unittest.main()



