"""
Electricity bill estimator
Enter cents per kWh: 35
Enter daily use in kWh: 4.5
Enter number of billing days: 90
Estimated bill: $141.75
"""
total = 0
price_per_kwh = int(input("Enter your price per kWh in cents: "))
daily_use = float(input("Enter your daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))

while total == 0:
    if price_per_kwh > 0:
        total = price_per_kwh/100 * daily_use * billing_days
        print("Estimated bill price is: $", total)
    else:
        print("Invalid Input")
print("Goodbye")
