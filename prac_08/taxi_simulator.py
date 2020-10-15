"""
CP1404/CP5632 Practical
taxi simulator
Daniel Mackenzie
"""

from prac_08.car import Car
from prac_08.taxi import Taxi
from prac_08.Silver_Service_Taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():

    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's drive!")
    print(MENU)
    menu_choice = input(">>> ").lower()
    while menu_choice != "q":

        if menu_choice == "c":
            print("Taxis available:")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            current_taxi = taxis[taxi_choice]

        elif menu_choice == "d":
            current_taxi.start_fare()
            distance = int(input("Drive how far? "))
            current_taxi.drive(distance)
            fare = current_taxi.get_fare()
            print("Your {} trip cost you ${:.2f}".format(current_taxi.name, fare))
            total_bill += fare

        else:
            print("Invalid Choices")
        print("Bill to date: S{:.2f}".format(total_bill))
        print(MENU)
        menu_choice = input(">>>").lower()

    print("Bill to date: S{:.2f}".format(total_bill))
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))
        # i spent an hour trying to find out what was wrong with my code i had taxis instead of taxi ahhhhhhhhh

main()
