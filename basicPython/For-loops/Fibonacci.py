firstItem = 0
secondItem = 1
sumOfValue = 0
for i in range(0, 400):
    sumOfValue = firstItem + secondItem
    if sumOfValue % 2 == 0:
        print(sumOfValue)
    firstItem = secondItem
    secondItem = sumOfValue

