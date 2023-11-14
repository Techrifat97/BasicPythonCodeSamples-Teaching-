#Use for, .split(), and if to create a Statement that will print out words that start with 's':

val_st = 'Print only the words that start with s in this sentence'
mylist = val_st.split(' ')
print(list)

for items in mylist:
    if items[0] == 's':
        print(items)
    else:
        pass


#Use range() to print all the even numbers from 0 to 10.
for num in range(0, 10):
    if num % 2 == 0:
        print(f"{num} is even")
        
# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

mySecondList = []

for num in range (1, 50):
    if num % 3 == 0:
        mySecondList.append(num)

print(mySecondList)