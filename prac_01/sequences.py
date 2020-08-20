"""
CP1404/CP5632 - Practical
electricity bill
Daniel Mackenzie
"""

x_input = int(input("Input X"))
y_input = int(input("Input y"))
if x_input % 2 == 1:
    x_input = - 1
num_choices = int(input("(1) Show the even numbers from x to y\n(2) Show the odd numbers from x to y\n(3) Show the squares from x to y\n(4) Exit the program"))
while num_choices != 4:
    if num_choices == 1:
        for i in range(x_input, y_input, 2):
            print(i, end=' ')
    elif num_choices == 2:
        for i in range(x_input, y_input, 2):
            print(i, end=' ')
    elif num_choices == 3:
        for i in range(x_input, y_input, 2):
            print(i, end=' ')
    else:
        print("invalid number")
    num_choices = int(input(
        "(1) Show the even numbers from x to y\n(2) Show the odd numbers from x to y\n(3) Show the squares from x to y\n(4) Exit the program"))
