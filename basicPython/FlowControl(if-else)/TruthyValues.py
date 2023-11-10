if 0:
    print("true")
else:
    print("false")

print("-" * 80)
name = input("What is your name? ")
# if name:
if name != "":  # empty string check
    print("Hi {0}!".format(name))
else:
    print("You dont have name")
