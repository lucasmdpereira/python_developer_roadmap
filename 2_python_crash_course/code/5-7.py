# 5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.

# Make a list of your three favorite fruits and call it favorite_fruits.

favorite_fruits = ['banana', 'avocado', 'orange']

# Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the if block should print a statement, such as You really like bananas!

test_fruits = ['banana', 'grapes', 'water mellon', 'apple', 'avocado']

for test_fruit in test_fruits:
    if test_fruit in favorite_fruits:
        print(f"You realy like {test_fruit}")
    else:
        print(f"You don't realy like {test_fruit}")
    
    

    