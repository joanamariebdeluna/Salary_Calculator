
def TotalPay_calculator(hourly_rate, hours_worked):
    if hourly_rate < 0 or hours_worked < 0:
        return hourly_rate * hours_worked
