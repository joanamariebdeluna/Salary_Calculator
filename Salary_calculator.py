
def Totalpay_calculator(hourly_rate, hours_worked):
    if hourly_rate < 0 or hours_worked < 0:
        return hourly_rate * hours_worked

def Tax_calculator(total_pay, tax_rate):
    if tax_rate < 0 or tax_rate > 1:
        return total_pay * tax_rate
    
def calculate_deductions(total_pay, deduction_rate):
    if deduction_rate < 0 or deduction_rate > 1:
        return total_pay * deduction_rate
    