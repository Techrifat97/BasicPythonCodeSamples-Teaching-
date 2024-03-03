shopping_list = ["Milk", "Pasta", "Eggs", "Spam", "Rice"]
for item in shopping_list:
    if "Spam" not in item:
        print("Buy " + item)
print('\n')
shopping_list = ["Milk", "Pasta", "Eggs", "Spam", "Rice"]
for item in shopping_list:
    if "Spam" in item:
        continue
    print("Buy " + item)
