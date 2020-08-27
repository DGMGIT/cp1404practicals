"""
CP1404/CP5632 Practical
refactor valid password to asterisks
Daniel Mackenzie
"""

MIN_LENTH = 3

def main():
    password = get_password(MIN_LENTH)
    print_asterisks(password)



def get_password(min_len):
    """get valid password, must meet MIN_LENTH"""
    password = input(f"Enter password must be at least {min_len} character long:")
    while len(password) < min_len:
        print("too short")
        password = input(f"Enter password must be at least {min_len} character long:")
    return password


def print_asterisks(password):
    """print len(password) as * """
    for CHARS in password:
        print("*", end="")


main()