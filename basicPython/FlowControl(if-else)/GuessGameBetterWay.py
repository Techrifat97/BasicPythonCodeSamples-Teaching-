answer = 5
guess = int(input("Enter your guessing number between 1 to 10: "))
if answer == guess:
    print("You made it first choice")
else:
    if guess > answer:
        guess = int(input("Guess a number lower "))
    else:
        guess = int(input("Guess a number higher "))
    if guess == answer:
        print('You are correct')
    else:
        print("you are wrong")
