min_length = 5
user_password = input("Enter your password: ")
while len(user_password) < min_length:
    print("Password is too short.")
    user_password = input("Enter your password: ")
star_length = len(user_password)
print(star_length * "*")
