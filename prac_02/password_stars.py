def main():
    min_length = 5
    user_password = get_password(min_length)
    print_password(user_password)


def print_password(user_password):
    print(len(user_password) * "*")


def get_password(min_length):
    user_password = input("Enter your password: ")
    while len(user_password) < min_length:
        print("Password is too short.")
        user_password = input("Enter your password: ")
    return user_password

main()
