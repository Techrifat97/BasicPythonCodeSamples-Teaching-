shopping_list = ["Milk", "Egg", "Bread", "Rice", "Spam", "Pasta", "Noodles"]
find_item = "Spam"
found_at_index = None
for index in range(len(shopping_list)):
    if shopping_list[index] == find_item:
        found_at_index = index
print(f"Item found in index: {found_at_index}")

shopping_list = ["Milk", "Egg", "Bread", "Rice", "Spam", "Pasta", "Noodles"]
find_item = "Spam"
found_at_index = None
for index in range(len(shopping_list)):
    if shopping_list[index] == find_item:
        found_at_index = index
        break
print(f"Item found in index: {found_at_index}")
