import unittest
from Salary_calculator import Salary_calculator

class SalaryCalculator_test(unittest.TestCase):
    def Totalpay_calculatorTest(self):
        calculator = Salary_calculator(50000, 0.2, 0.1)
        self.assertEqual(calculator.calculate_total_pay(), 50000)

    def Tax_calculatorTest(self):
        calculator = Salary_calculator(50000, 0.2, 0.1)
        self.assertEqual(calculator.calculate_tax(), 10000)

    def Deduction_calculatorTest(self):
        calculator = Salary_calculator(50000, 0.2, 0.1)
        self.assertEqual(calculator.calculate_deductions(), 5000)

    def Netpay_calculatorTest(self):
        calculator = Salary_calculator(50000, 0.2, 0.1)
        self.assertEqual(calculator.calculate_net_pay(), 35000)

    def Zero_grosspayTest(self):
        calculator = Salary_calculator(0, 0.2, 0.1)
        self.assertEqual(calculator.calculate_net_pay(), 0)

    def Negative_grosspayTest(self):
        with self.assertRaises(ValueError):
            Salary_calculator(-1000, 0.2, 0.1)


if __name__ == '__main__':
    unittest.main()