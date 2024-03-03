# checking number is even or not using function

def even_check_fucntion(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("ODD")


print("Can you Input a Number to check either it is even or not?\n")
num = int(input())
even_check_fucntion(num)

#checking number is even or not in a list:

def check_number_even(myList):
    myEvenNumList = [] #place holder for list
    for number in myList:
        if number % 2 == 0:
            myEvenNumList.append(number)
        else:
            pass
    return myEvenNumList

myList = [1,2,3,4,5,6,7,8]
myNewList = check_number_even(myList)
print(myNewList)

myNewUpList = [num  for num in myList if num % 2 == 0 ] # list comprehension
print(myNewUpList)


# fuction using list comprehension
def check_even(myList):
    myNew2ndList = [num  for num in myList if num % 2 == 0 ]
    return myNew2ndList

print(check_even(myList))