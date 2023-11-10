age = int(input("Please give your age: "))
# if age >= 16 and  age <= 65:    // for and python stop condition if it finds false
if 16 <= age <= 65:
    print('You can work')
else:
    print("You can not work")
print("-" * 80)

if age < 16 or age > 65:    # in or python stop condition if it finds one true
    print("Enjoy your free time")
else:
    print("You can work")
