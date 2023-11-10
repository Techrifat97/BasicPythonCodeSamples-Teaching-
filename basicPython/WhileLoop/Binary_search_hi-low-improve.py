high = 1000
low = 1
print(f"Guess a number between {low} to {high}:")
input("Enter to continue")
guess = 0
while high != low:
    middle = low +(high - low) // 2
    print(f"if your guess number is higher then computer guess {middle} then press h "
    "or lower then guess type l"
    "or correct press c")
    user_input = input()
    if user_input == "h":
        low = middle + 1
    elif user_input == "l":
        high = middle - 1
    elif user_input =='c':
        print(f"Your guess is {middle}")
        break
    else:
        print("Please select something")
    guess +=1
else:
    print(f"Your thought is {low}")
    print(f"we guess your number in {guess} times")