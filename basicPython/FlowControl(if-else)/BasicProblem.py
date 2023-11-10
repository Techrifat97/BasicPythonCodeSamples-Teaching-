name = input("What is your name? ")
age = int(input(f"What is your age, {name}? "))
if 18 <= age < 31:
    print("Welcome to holiday!")
else:
    print("Please! come later in future! ")

print("cookie \n" * 3)

condition  = True
if condition:
    print("The condition is true")
else:
    print("The condtion is false")

print(f"Are you hungry {name}?")
answer = str(input("Type yes or no:"))

if answer == "yes":
    print(f"give food to {name}")
else:
    print("let me know when you are hungry")
