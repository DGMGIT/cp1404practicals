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
