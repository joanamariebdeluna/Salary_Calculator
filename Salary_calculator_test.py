import unittest
from Salary_calculator import Salary_calculator

class SalaryCalculator_test(unittest.TestCase):
    def Totalpay_calculatorTest(self):
        calculator = Salary_calculator(50000, 0.2, 0.1)
        self.assertEqual(calculator.Totalpay_calculator(), 50000)

    def Tax_calculatorTest(self):
        calculator = Salary_calculator(50000, 0.2, 0.1)
        self.assertEqual(calculator.Tax_calculator(), 10000)

    def Deduction_calculatorTest(self):
        calculator = Salary_calculator(50000, 0.2, 0.1)
        self.assertEqual(calculator.Deduction_calculator(), 5000)

    def Netpay_calculatorTest(self):
        calculator = Salary_calculator(50000, 0.2, 0.1)
        self.assertEqual(calculator.Netpay_calculator(), 35000)

    def Zero_grosspayTest(self):
        calculator = Salary_calculator(0, 0.2, 0.1)
        self.assertEqual(calculator.Netpay_calculator(), 0)

    def Negative_grosspayTest(self):
        with self.assertRaises(ValueError):
            Salary_calculator(-1000, 0.2, 0.1)


if __name__ == '__main__':
    unittest.main()
    