#Use for, .split(), and if to create a Statement that will print out words that start with 's':

val_st = 'Print only the words that start with s in this sentence'
mylist = val_st.split(' ')
print(list)

for items in mylist:
    if items[0] == 's':
        print(items)


#Use range() to print all the even numbers from 0 to 10.
for num in range(0, 10):
    if num % 2 == 0:
        print(f"{num} is even")
print(list(range(0,11,2)))
# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

mySecondList = []

for num in range (1, 50):
    if num % 3 == 0:
        mySecondList.append(num)

print(mySecondList)

# Optional option: 

myThirdList = [num for num in range(1,50) if num % 3 == 0]
print(myThirdList)

#Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
mySplittedList = st.split(' ')
for num in mySplittedList:
    if len(num) % 2 == 0:
        print(f'This word is even: {num}')
    else:
        print(f"This word is ODD: {num}")        
print('*' * 50)

# Write a program that prints the integers from 1 to 100. 
# But for multiples of three print "Fizz" instead of the number, 
# and for the multiples of five print "Buzz". 
# For numbers which are multiples of both three and five print "FizzBuzz"

for num in range(1, 100):
    if num % 3 == 0 and num % 5 == 0:
        print ("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num & 5 == 0:
        print("Buzz")
    else:
        print(num)
        
#Use List Comprehension 
# to create a list of the first letters 
# of every word in the string below:
newSt = 'Create a list of the first letters of every word in this string'
mySpList = newSt.split(' ')
myAddList = []

for items in mySpList:
    myAddList.append(items[0])
print(myAddList)

#second option
myAddList = [items[0] for items in mySpList]
print(myAddList)

for words in newSt.split(' '):
    if len(words) % 2 == 0:
        print(f"{words} is even")