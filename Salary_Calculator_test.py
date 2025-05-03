
from Salary_Calculator import Salary_Calculator

from Salary_Calculator import (
    calculate_total_pay,
    calculate_tax,
    calculate_deductions,
    calculate_net_pay,
)

def test_calculate_total_pay():
    assert calculate_total_pay(15, 40) == 600
    with pytest.raises(ValueError):
        calculate_total_pay(-10, 20)

def test_calculate_tax():
    assert calculate_tax(600, 0.2) == 120
    with pytest.raises(ValueError):
        calculate_tax(600, 1.2)

def test_calculate_deductions():
    assert calculate_deductions(600, 0.1) == 60
    with pytest.raises(ValueError):
        calculate_deductions(600, -0.1)

def test_calculate_net_pay():
    assert calculate_net_pay(600, 120, 60) == 420