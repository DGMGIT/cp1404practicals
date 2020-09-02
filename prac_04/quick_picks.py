"""
CP1404/CP5632 Practical
quick picks
Daniel Mackenzie
"""


import random


LINE_LENGTH = 6
MIN = 1
MAX = 45


def main():
    quick_pick_num = get_valid_num()
    generate_quick_picks(quick_pick_num)


def get_valid_num():
    num = int(input("How many quick picks? "))
    while num <= 0:
        print("nvalid number")
        num = int(input("How many quick picks? "))
    return num


def generate_quick_picks(quick_pick_num):
    for i in range(quick_pick_num):
        quick_pick = []
        for j in range(LINE_LENGTH):
            random_num = random.randint(MIN, MAX)
            while random_num in quick_pick:
                random_num = random.randint(MIN, MAX)
            quick_pick.append(random_num)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))


main()