
from Salary_Calculator import Salary_Calculator

from Salary_Calculator import (
    TotalPay_calculator,
)

def test_calculate_total_pay():
    assert TotalPay_calculator(15, 40) == 600
    TotalPay_calculator(-10, 20)
        