    
class Salary_calculator:
    def __init__(self, gross_pay, tax_rate, deduction_rate):
        self.gross_pay = gross_pay
        self.tax_rate = tax_rate
        self.deduction_rate = deduction_rate

    def Totalpay_calculator(self):
        return self.gross_pay

    def Tax_calculator(self):
        return self.gross_pay * self.tax_rate

    def Deduction_calculator(self):
        return self.gross_pay * self.deduction_rate

    def Netpay_calculator(self):
        return self.gross_pay - self.calculate_tax() - self.calculate_deductions()
    