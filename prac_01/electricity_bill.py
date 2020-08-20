"""
CP1404/CP5632 - Practical
electricity bill
Daniel Mackenzie
"""

# print("Electricity bill estimator")
# price_per_kwh = int(input("Enter cents per kWh: "))
# daily_use_kwh = float(input("Enter daily use in kWh: "))
# num_billing_days = int(input("Enter number of billing days: "))
# price_per_kwh_cents = price_per_kwh / 100
# estimated_bill = price_per_kwh_cents * daily_use_kwh * num_billing_days
# print("Estimated bill: ", estimated_bill)

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator 2.0")
price_per_kwh = int(input("Which tariff? 11 or 31: "))
while price_per_kwh != 11 and price_per_kwh != 31:
    print("invalid choice")
    price_per_kwh = int(input("Which tariff? 11 or 31: "))
daily_use_kwh = float(input("Enter daily use in kWh: "))
num_billing_days = int(input("Enter number of billing days: "))
if price_per_kwh == 11:
    price_per_kwh_cents = TARIFF_11
else:
    price_per_kwh_cents = TARIFF_31
estimated_bill = price_per_kwh_cents * daily_use_kwh * num_billing_days
print("Estimated bill: {:.2f}".format(estimated_bill))
