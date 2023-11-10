Shopping_list = ['book', 'pan', 't-shirt', 'milk']
find_item = "pan"
find_item_index = None
if find_item in Shopping_list:
    find_item_index = Shopping_list.index(find_item)

if find_item_index is not None:
    print(f"Item found at index{find_item_index}")
else:
    print("item not found")
