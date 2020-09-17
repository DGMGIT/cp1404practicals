"""
CP1404/CP5632 Practical
Guitars! test
Daniel Mackenzie
"""

from prac_06.guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
another = Guitar("Another Guitar", 2013)


print(f"Gibson L-5 CES get_age() - Expected 95. Got {gibson.get_age()}")
print(f"Another Guitar get_age() - Expected 7. Got {another.get_age()}")

print(f"Gibson L-5 CES is_vintage() - Expected True. Got {gibson.is_vintage()}")
print(f"Another Guitar is_vintage() - Expected False. Got {another.is_vintage()}")