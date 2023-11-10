for i in range(0, 11):
    print(i)
print("*" * 100)
for i in range(0, 11, 2):
    print(i)
print("*" * 100)
for i in range(10, 0, -2):
    print(i)
print("*" * 100)

age = int(input("Your age is : "))
if age in range(16, 66):
    print("Enjoy your Work Life")
else:
    print("Enjoy your free time")
