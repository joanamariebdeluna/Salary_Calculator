def TotalPay_calculator(hourly_rate, hours_worked):
    if hourly_rate < 0 or hours_worked < 0:
        raise ValueError("Hourly rate and hours worked cannot be negative.")
    return hourly_rate * hours_worked
