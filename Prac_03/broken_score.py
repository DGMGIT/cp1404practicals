"""
CP1404/CP5632 Practical
refactor program to determine score status
Daniel Mackenzie
"""


def main():
    score = float(input("Enter score: "))
    print(determine_grade(score))


def determine_grade(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return"Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


main()