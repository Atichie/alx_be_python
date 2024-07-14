import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

        def setup(self):
            self.calc = SimpleCalculator()

        def test_addition(self):
            calc = SimpleCalculator()
            result = calc.add(2, 3)
            self.assertEqual(result, 5)

        def test_subtract(self):
            calc = SimpleCalculator()
            result = calc.subtract(5, 3)
            self.assertEqual(result, 2)

        def test_multiply(self):
            calc = SimpleCalculator()
            result = calc.multiply(5, 3)
            self.assertEqual(result, 15)

        def test_divide(self):
            calc = SimpleCalculator()
            try:
                calc.divide(5, 0)
                self.fail("Expected ZeroDivisionError")
            except ZeroDivisionError as e:
                self.assertEqual(str(e), "division by zero")
            
    

name = "_main_"
if name == "_main_":
    unittest.main()



