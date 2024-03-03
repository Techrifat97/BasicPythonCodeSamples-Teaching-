from random import shuffle

myList = [' ', ' ', 'O']

def shuffle_list(myList):
    shuffle(myList)    
    return myList

def player_guess():
    guess = ' '
    while guess not in ['0','1','2']:
        guess = input("Guess Your number From(0, 1, 2) and type one of the number")
    return int(guess)



def check_validity():
    shuffledList = shuffle_list(myList)
    print(shuffledList)
    guess = player_guess()
    
    if shuffledList[guess] == 'O':
        return ("You WIN!")
    else:
        return ("You LOST")

print(check_validity())

