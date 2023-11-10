import random

answer = random.randint(1, 100)
print(answer)
print("if you want to exit from the game, please type 0 ")
user_input = int(input("Please type a number"))

if answer == user_input:
    print("you are correct")
else:
    while user_input != answer:
        if user_input == 0:
            break
        elif answer > user_input:
            print("choose a higher value: ")
            user_input = int(input("Please type a number"))
            if user_input == answer:
                print("You are right this time")
                break
        elif answer < user_input:
            print("choose a lower value: ")
            user_input = int(input("Please type a number"))
            if user_input == answer:
                print("You are right this time")
                break
