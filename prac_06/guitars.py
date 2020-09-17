"""
CP1404/CP5632 Practical
Guitars!
Daniel Mackenzie
"""

from prac_06.guitar import Guitar


def main():  # i did start it before reading the notes
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("year: "))
        cost = float(input("cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(guitar, "added.\n")
        name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        print("\nThese are my guitars:")
        num = 0
        guitars.sort()
        for guitar in guitars:
            num += 1
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = " (vintage)"
            print(guitar, vintage_string)

    # if guitars:  # lists, strings and other collections are False when empty, True when non-empty
    #     # In order for sorting to work on Guitar objects,
    #     # at least the __lt__ method must be defined in Guitar class
    #     guitars.sort()
    #     print("These are my guitars:")
    #     for i, guitar in enumerate(guitars):
    #         vintage_string = ""
    #         if guitar.is_vintage():
    #             vintage_string = "(vintage)"
    #         print("Guitar {0}: {1.name:>30} ({1.year}), worth ${1.cost:10,.2f}\
    #            {2}".format(i + 1, guitar, vintage_string))
    else:
        print("No guitars :( Quick, go and buy one!")

main()