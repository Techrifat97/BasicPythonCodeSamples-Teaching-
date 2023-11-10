print("Guess Game for computer")
print("High value is 1000 and low is 1")
high = 1000
low = 1
input("Enter to continue")
guess = 1
while True:
    middle_point = low + (high - low) // 2
    print(f"computer  guess is {middle_point} "
          f"if your guess is higher then this type 'h' "
          f"if your guess is lower than this press l"
          f"if your guess is matched then type 'c'")
    value = input('type: ')
    if value == 'h':
        low = middle_point + 1
    elif value == "l":

        high = middle_point - 1
    elif value == 'c':
        print("ok done")
        break

