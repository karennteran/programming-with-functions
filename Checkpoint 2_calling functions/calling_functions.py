import math

number_items = int(input("Enter the number of items: "))
items_per_box = int(input("Enter the number of items per box: "))
print()
number_of_boxes = math.ceil(number_items / items_per_box)
print()
print(f"for {number_items} items, packing {items_per_box} items in each box, you will need {number_of_boxes} boxes.")
print()
