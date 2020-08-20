"""
CP1404/CP5632 - Practical
menus
Daniel Mackenzie
"""
name = input("Enter name :")
choice = input("(H)ello\n(G)oodbye\n(Q)uit\n>>>").upper()
while choice != "Q":
   if choice == "H":
       print("hello ", name)
   elif choice == "G":
       print("goodbye ", name)
   else:
       print("invalid message")
   choice = input("(H)ello\n(G)oodbye\n(Q)uit\n>>>").upper()
print("Finished.")