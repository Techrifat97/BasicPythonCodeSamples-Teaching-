numbers = [1,31,15,19]
for number in numbers:
    if number % 8 == 0:
        print("This number is not acceptable")
        break
else:
    print("This number is acceptable")