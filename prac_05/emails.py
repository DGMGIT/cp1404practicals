"""
CP1404/CP5632 Practical - Suggested Solution
emails
Daniel Mackenzie
"""

email_and_name = {}


def main():
    email = input("Email: ")
    while email != "":
        if email in email_and_name:
            print("email already added")
        else:
            user_name = get_name(email)
            email_and_name[email] = check_user_name(user_name)
        email = input("Email: ")
    for email in email_and_name:
        print("{} ({})".format(email_and_name[email], email))


def get_name(email):
    """splits email to fine username"""
    parts = email. split("@")[0].split(".")
    name = " ".join(parts).title()
    return name


def check_user_name(user_name):
    """checks username"""
    username_check = input(f"is this your name {user_name} (Y/N) ").upper()
    if username_check[0] == "N":
        user_name = input("name: ")
    return user_name


main()
