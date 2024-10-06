# Q.1
name = input("Enter your name: ")
file = open("name.txt", 'w')
print(name, file = file)
file.close()

# Q.2
file = open("name.txt", 'r')
name = file.read()
print(f"Hi {name}!")
file.close()

# Q.3
with open("numbers.txt", "r") as file:
    first_line = int(file.readline())
    second_line = int(file.readline())
    print(first_line + second_line)

#  Q.4
total = 0
with open("numbers.txt", 'r') as file:
    for line in file:
        number = int(line)
        total += number
    print(total)