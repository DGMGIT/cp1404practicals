"""
CP1404/CP5632 Practical - Suggested Solution
Hex colours
Daniel Mackenzie
"""

COLOURS = {"AliceBlue": "f0f8ff", "beige": "f5f5dc", "black": "000000", "DarkGreen": "006400", "BlueViolet": "8a2be2",
           "brown": "a52a2a", "burlywood": "deb887", "CadetBlue": "5f9ea0", "chocolate": "d2691e", "coral": "ff7f50"}

colour = input("colour name: ")
while colour != "":
    if colour in COLOURS:
        print(f"{colour} is #{COLOURS[colour]}")
    else:
        print("invalid input")
    colour = input("colour name: ")
