import pytest
from Salary_Calculator import Salary_Calculator

from Salary_Calculator import (
    Totalpay_calculator
)

def test_calculate_total_pay():
    assert Totalpay_calculator(15, 40) == 600
        Totalpay_calculator(-10, 20)
