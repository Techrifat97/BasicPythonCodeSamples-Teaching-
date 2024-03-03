# Level 2 problems
def has_33(myList):
    for index, item in enumerate(myList):
        if item == 3 and index +1 < len(myList):
            index += 1
            if myList[index] == 3:
                return True  
            else:
                continue
        else:
            continue
    return False
    
myList = [3,1,3]
print(has_33(myList))


def paper_doll(text):
    textString = text
    strnewValue = []
    for char in textString:
         strnewValue.append(char * 3)
    
    return strnewValue

newList = paper_doll("hello")
myvalue = "".join(newList)
print(myvalue)

def BlackJack(a,b,c):
    sum = a + b + c
    
    if sum <= 21:
        return sum
    elif sum > 21:
        if a == 11 or b == 11 or c == 11:
            sum = sum - 10
            if sum >= 21:
                return "bust"
            else:
                return sum
        else:
            return "Bust"
    else:
        return 'bust'

print(BlackJack(9,9,11))
