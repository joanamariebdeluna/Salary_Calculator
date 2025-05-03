
def TotalPay_calculator(hourly_rate, hours_worked):
    if hourly_rate < 0 or hours_worked < 0:
        raise ValueError("Hourly rate and hours worked cannot be negative.")
    return hourly_rate * hours_worked

def Tax_calculator(total_pay, tax_rate):
    if tax_rate < 0 or tax_rate > 1:
        raise ValueError("Tax rate must be between 0 and 1.")
    return total_pay * tax_rate

def Deductions_calculation(total_pay, deduction_rate):
    if deduction_rate < 0 or deduction_rate > 1:
        raise ValueError("Deduction rate must be between 0 and 1.")
    return total_pay * deduction_rate

def Netpay_calculator(total_pay, tax, deductions):
    return total_pay - tax - deductions
