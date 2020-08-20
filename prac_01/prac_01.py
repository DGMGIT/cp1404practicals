"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print("Result: {:.2f} F".format(fahrenheit))
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = 5 / 9 * (fahrenheit - 32)
        print("Result: {:.2f} C".format(celsius))
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")


"""
CP1404/CP5632 - Practical
sales bonus
Daniel Mackenzie
"""
"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales: $"))
bonus = 0
while sales >= 0:
    if sales < 1000:
        bonus = sales * 0.10
    else:
        bonus = sales * 0.15
    print(f"bonus is {bonus}")
    sales = float(input("Enter sales: $"))


"""
CP1404/CP5632 - Practical
Broken program to determine score status
Daniel Mackenzie
"""

score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
elif score < 50:
    print("Bad")
elif score < 90:
    print("Passable")
else:
    print("Excellent")


"""
CP1404/CP5632 - Practical
loops
Daniel Mackenzie
"""

for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

stars = int(input("number of stars: "))
for i in range(stars):
    print("*", end='')

stars = int(input("number of stars: "))
for i in range(0, stars + 1):
    print("*" * i)


"""
CP1404/CP5632 - Practical
shop calculator
Daniel Mackenzie
"""
total_cost =0
num_items = int(input("Number of items :"))
for i in range(num_items):
    costs = float(input("Prices of items: "))
    total_cost += costs
if total_cost > 100:
    discount = total_cost * 0.10
    total_cost = total_cost - discount
print("Total price for {} items is ${:.2f}".format(num_items, total_cost))


"""
CP1404/CP5632 - Practical
menus
Daniel Mackenzie
"""
name = input("Enter name :")
choice = input("(H)ello\n(G)oodbye\n(Q)uit\n>>>").upper()
while choice != "Q":
    if choice == "H":
        print("hello ", name)
    elif choice == "G":
        print("goodbye ", name)
    else:
        print("invalid message")
    choice = input("(H)ello\n(G)oodbye\n(Q)uit\n>>>").upper()
print("Finished.")


"""
CP1404/CP5632 - Practical
electricity bill
Daniel Mackenzie
"""

print("Electricity bill estimator")
price_per_kwh = int(input("Enter cents per kWh: "))
daily_use_kwh = float(input("Enter daily use in kWh: "))
num_billing_days = int(input("Enter number of billing days: "))
price_per_kwh_cents = price_per_kwh / 100
estimated_bill = price_per_kwh_cents * daily_use_kwh * num_billing_days
print("Estimated bill: ", estimated_bill)

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
