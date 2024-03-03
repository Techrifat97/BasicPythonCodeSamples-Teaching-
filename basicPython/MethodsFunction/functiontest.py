def lineGap():
    print('\n')
    print('*' * 50)
    print('\n')
    
    
def less_even(a,b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a,b)
    else:
        return max(a,b)

value = less_even(2,6)
print(value)

lineGap()

def animal_crackers(val):
    nameList =val.split(" ")
    return nameList[0][0] == nameList[1][0]

print(animal_crackers("shaon suhi"))

lineGap()

def makes_twenty(a,b):
    return a + b == 20 or a == 20 or b == 20

print(makes_twenty(12,8))

lineGap()

def old_macDonald(val):
    name = ''
    it = len(val)
    for  i in range(0, it):
        if i == 0:
            name = name + val[i].capitalize()
            continue
        if i == 3:
            name = name + val[i].capitalize()
            continue
        name = name + val[i]
    return name

print(old_macDonald('macdonald'))

lineGap()
def old_mac(value):
    if len(value) > 3:
        return  value[0].capitalize() + value[1:3]+value[3].capitalize() + value[4:]
    else:
        return print("please put a value ")

print(old_mac('macdonald'))

lineGap()

def string_split(value):
    return value.split(' ')
    


def reverse_word():
    mylist = string_split("I am Home")
    mylist.reverse()
    name = " ".join(mylist)
    return name

print(reverse_word())

lineGap()

def almostThere(value):
   return value in range(90, 110) or value in range(190,210)

print(almostThere(200))

lineGap()


