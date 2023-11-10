# You are eligible to vote or not
name = input("Please enter your name:")
age = int(input(f"Dear {name} , enter your age: "))

if age < 18:
    print(f"Dear {name}, come back after {18 - age} years")
elif age == 900:
    print("You are not human at all")
else:
    print(f"Dear {name}, You are eligible to vote")
