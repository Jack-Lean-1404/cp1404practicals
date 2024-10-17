# Guess = 25mins and 25sec
# Actual =

def main():
    """Create emails_to name dictionary"""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        review = input(f"Is your name {name}? (Y/n) ")
        if review.upper() != "Y" and review != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")

def get_name_from_email(email):
    """Extract name from email"""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name

main()

