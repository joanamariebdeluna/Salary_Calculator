
from Salary_calculator import Salary_calculator

from Salary_calculator import (
    Totalpay_calculator,
    Tax_calculator,
    Deduction_calculator,
)

def Totalpay_calculator_test():
    assert Totalpay_calculator(15, 40) == 600
    Totalpay_calculator(-10, 20)
    
def Tax_calculator():
    assert Tax_calculator(600, 0.2) == 120
    Tax_calculator(600, 1.2)
    
def Deduction_calculation():
    assert Deduction_calculation(600, 0.1) == 60
    Deduction_calculation(600, -0.1)
    