"""
CP1404/CP5632 Practical
Intermediate Exercises
Daniel Mackenzie
"""


# numbers
num_list = []
for i in range(5):
    num = int(input("Number: "))
    num_list.append(num)

print(f"The first number is {num_list[0]}")
print(f"The last number is {num_list[-1]}")
print(f"The smallest number is {min(num_list)}")
print(f"The largest number is {max(num_list)}")
print(f"The average of the numbers is {sum(num_list) / len(num_list)}")


usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
valid_usernames = input("usernames: ")
while valid_usernames not in usernames:
    print("Access denied")
    valid_usernames = input("usernames: ")
print("Access granted")
