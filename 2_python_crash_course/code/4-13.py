# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.

basic_foods = ("rice","beans","steak","fries","vegetables")

# Use a for loop to print each food the restaurant offers.

print("")
for food in basic_foods:
    print(food.title())
    
# basic_foods[0] = "forbidden"

# The restaurant changes its menu, replacing two of the items with different foods. Add a line that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.

basic_foods = ("rice","peas","steak","pasta","vegetables")
print("")
for food in basic_foods:
    print(food.title())

