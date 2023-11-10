answer = 7
print("Enter your guessing number:")
guess = int(input())
if guess < answer:
    print("try to choose a higher number")
    guess2 = int(input("Guess another higher number:"))
    if guess2 == answer:
        print("You made it in 2nd choice")
    else:
        print("Sorry you guessed it wrong")
elif guess > answer:
    print("try to choose a lower number ")
    guess2 = int(input("Guess another lower number:"))
    if guess2 == answer:
        print("You made it in 2nd choice")
    else:
        print("Sorry you guessed it wrong")
else:
    print("You guess it first time")
