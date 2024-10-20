# Guess = 25mins and 25sec
# Actual = ???

def main():
    """Create a dictionary of names and emails"""
    name_to_email = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        review = input(f"Is your name {name}? (Y/n) ")
        if review.upper() != "Y" and review != "":
            name = input("Name: ")
        name_to_email[email] = name
        email = input("Email: ")

    for email, name in name_to_email.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    """Return prefix from email"""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    return " ".join(parts).title()


main()
