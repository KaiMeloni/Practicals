"""
Electricity bill estimator 2.0
Which tariff? 11 or 31: 11
Enter daily use in kWh: 13.4
Enter number of billing days: 90
Estimated bill: $295.01
"""

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

total = 0
price_per_kwh = float(input("Which Tariff do you use?\n1.TARIFF_11 = 0.244618\n2.TARIFF_31 = 0.136928\nEnter:"))
daily_use = float(input("Enter your daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))

while total == 0:
    if price_per_kwh == 1:
        total = TARIFF_11 * daily_use * billing_days
        print("Estimated bill price is: $", total)
    elif price_per_kwh == 2:
        total = TARIFF_31 * daily_use * billing_days
        print("Estimated bill price is: $", total)
    else:
        print("Invalid Input")

