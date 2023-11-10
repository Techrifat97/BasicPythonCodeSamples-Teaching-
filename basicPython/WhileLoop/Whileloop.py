i = 0
while i != 10:
    print(i)
    i += 1

chosen_list = ["south", 'East', 'west', 'north']
item = ''
while item.casefold() not in chosen_list:
    item = input("Please put your direction")

print("You have done")
