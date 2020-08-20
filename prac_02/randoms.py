"""
CP1404/CP5632 - Practical
randoms
Daniel Mackenzie
"""

import random

print(random.randint(5, 20))
print(random.randrange(3, 10, 2))
print(random.uniform(2.5, 5.5))

# What did you see on line 1? 14
# What was the smallest number you could have seen, what was the largest? 5 20

# What did you see on line 2? 7
# What was the smallest number you could have seen, what was the largest? 3 9
# Could line 2 have produced a 4?

# What did you see on line 3? 2.863544744347552
# What was the smallest number you could have seen, what was the largest? 2.5 5.5

print(random.randint(1, 100))
print(random.randint(1, 2))