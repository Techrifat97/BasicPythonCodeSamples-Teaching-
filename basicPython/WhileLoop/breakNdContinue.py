import random
answer = random.randint(1,10)
i = 0
while i != 2:
    guess = int(input("Enter your guess number: "))
    if guess == answer:
        print("you are correct")
        break
    i += 1

