# **Summary**

1. []()
2. [VARIABLES AND SIMPLE DATA TYPES](#2-variables-and-simple-data-types)  
3. [INTRODUCING LISTS](#3-introducing-lists)  
    3.1. [Accessing Elements in a List](#31-accessing-elements-in-a-list)  
    3.2. [Using Individual Values from a List](#32-using-individual-values-from-a-list)  
    3.3. [Adding Elements to a List](#33-adding-elements-to-a-list)    
        &nbsp;&nbsp;&nbsp;3.3.1. [Appending Elements to the End of a List](#331-appending-elements-to-the-end-of-a-list)  
        &nbsp;&nbsp;&nbsp;3.3.2. [Inserting Elements into a List](#332-inserting-elements-into-a-list)  
    3.4. [Removing Elements from a List](#34-removing-elements-from-a-list)  
        &nbsp;&nbsp;&nbsp;3.4.1. [Removing an Item Using the del Statement](#341-removing-an-item-using-the-del-statement)  
        &nbsp;&nbsp;&nbsp;3.4.2. [Removing an Item Using the pop() Method](#342-removing-an-item-using-the-pop-method)  
        &nbsp;&nbsp;&nbsp;3.4.3. [Removing an Item by Value](#343-removing-an-item-by-value)  
    3.5. [Organizing a List](#35-organizing-a-liste)  
        &nbsp;&nbsp;&nbsp;3.5.1. [Sorting a List Permanently with the sort() Method](#351-sorting-a-list-permanently-with-the-sort-method)  
        &nbsp;&nbsp;&nbsp;3.5.2. [Sorting a List Temporarily with the sorted() Function](#352-sorting-a-list-temporarily-with-the-sorted-function)  
        &nbsp;&nbsp;&nbsp;3.5.3. [Reverse the original order of a list](#353-reverse-the-original-order-of-a-list)  
        &nbsp;&nbsp;&nbsp;3.5.4. [Finding the Length of a List](#354-finding-the-length-of-a-list)  
4. [WORKING WITH LISTS](#4-working-with-lists)  
    4.1. [Looping Through an Entire List](#41-looping-through-an-entire-list)      
    4.2. [Using the range() Function](#42-using-the-range-function)  
        &nbsp;&nbsp;&nbsp;4.2.1. [Using range() to Make a List of Numbers](#421-using-range-to-make-a-list-of-numbers)  
    4.3. [Simple Statistics with a List of Numbers](#43-simple-statistics-with-a-list-of-numbers)  
    4.4. [List Comprehensions](#44-list-comprehensions)  
    4.5. [Working with Part of a List](#45-working-with-part-of-a-list)  
        &nbsp;&nbsp;&nbsp;4.5.1. [Slicing a List](#451-slicing-a-list)  
        &nbsp;&nbsp;&nbsp;4.5.2. [Looping Through a Slice](#452-looping-through-a-slice)  
        &nbsp;&nbsp;&nbsp;4.5.3. [Copying a List](#453-copying-a-list)  
    4.6. [Tuples](#46-tuples)  
        &nbsp;&nbsp;&nbsp;4.6.1. [Defining a Tuple](#461-defining-a-tuple)  
        &nbsp;&nbsp;&nbsp;4.6.2. [Writing Over a Tuple](#462-writing-over-a-tuple)  
5. [IF STATEMENTS](#5-if-statements)  
    5.1. [Conditional Tests](#51-conditional-tests)  
        &nbsp;&nbsp;&nbsp;5.1.1. [Checking for Equality](#511-checking-for-equality)  
        &nbsp;&nbsp;&nbsp;5.1.2. [Checking for Inequality](#512-checking-for-inequality)  
        &nbsp;&nbsp;&nbsp;5.1.3. [Numerical Comparisons](#513-numerical-comparisons)  
        &nbsp;&nbsp;&nbsp;5.1.4. [Using and to Check Multiple Conditions](#514-using-and-to-check-multiple-conditions)  
        &nbsp;&nbsp;&nbsp;5.1.5. [Using or to Check Multiple Conditions](#515-using-or-to-check-multiple-conditions)  
    5.2. [Checking Whether a Value Is in a List](#52-checking-whether-a-value-is-in-a-list)  
    5.3. [Checking Whether a Value Is Not in a List](#53-checking-whether-a-value-is-not-in-a-list)  
    5.4. [Boolean Expressions](#54-boolean-expressions)  
    5.5. [Simple if Statements](#55-simple-if-statements)  
    5.6. [The if-elif-else Chain](#56-the-if-elif-else-chain)  
6. [DICTIONARIES](#6-dictionaries)  
    6.1. [A Simple Dictionary](#61-a-simple-dictionary)  
    6.2. [Adding New Key-Value Pairs](#62-adding-new-key-value-pairs)  
    6.3. [Modifying Values in a Dictionary](#63-modifying-values-in-a-dictionary)  
    6.4. [Removing Key-Value Pairs](#64-removing-key-value-pairs)  
    6.5. [Using get() to Access Values](#65-using-get-to-access-values)  
---

## 2.    VARIABLES AND SIMPLE DATA TYPES

Variable names can contain only letters, numbers, and underscores. They can start with a letter or an underscore, but not with a number. For instance, you can call a variable ```message_1``` but not ```1_message```.

Spaces are not allowed in variable names, but underscores can be used to separate words in variable names. For example, ```greeting_message``` works but ```greeting message``` will cause errors.

**The Python variables you’re using at this point should be lowercase.**

## 3. INTRODUCING LISTS

A list is a collection of items in a particular order.

Because a list usually contains more than one element, it’s a good idea to make the name of your list plural, such as ```letters```, ```digits```, or ```names```.

Square brackets ([]) indicate a list, and individual elements in the list are separated by commas.

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles) # ['trek', 'cannondale', 'redline', 'specialized']
```

### 3.1. Accessing Elements in a List

you can access any element in a list by telling Python the position
of the item desired.

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0]) # trek
```

### 3.2. Using Individual Values from a List

You can use individual values from a list just as you would any other variable. For example, you can **use f-strings** to create a message based on a value from a list.

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}."

print(message) # My first bicycle was a Trek.
```

### 3.3. Adding Elements to a List

#### 3.3.1. Appending Elements to the End of a List

The simplest way to add a new element to a list is to append the item to the list. The new element is added to the end of the list.

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) # ['honda', 'yamaha', 'suzuki']

motorcycles.append('ducati')
print(motorcycles) # ['honda', 'yamaha', 'suzuki', 'ducati']
```

#### 3.3.2. Inserting Elements into a List

You can add a new element at any position in your list by using the ```insert()``` method. 

```python
motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, 'ducati')
print(motorcycles) # ['ducati', 'honda', 'yamaha', 'suzuki']
```

### 3.4. Removing Elements from a List

#### 3.4.1. Removing an Item Using the del Statement

If you know the position of the item you want to remove from a list, you can use the ```del``` statement.

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) # ['honda', 'yamaha', 'suzuki']

del motorcycles[0]
print(motorcycles) # ['yamaha', 'suzuki']
```

#### 3.4.2. Removing an Item Using the pop() Method

The ```pop()``` method removes the an item in a list, but it lets you work with that item after removing it. If you use only ```pop()``` method removes the last item. If you pass a argument like ```pop(0)``` method removes the element.

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) # ['honda', 'yamaha', 'suzuki']

popped_motorcycle = motorcycles.pop()
print(motorcycles) # ['honda', 'yamaha']
print(popped_motorcycle) # suzuki
```

```python
motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.") # The first motorcycle I owned was a Honda.
```

#### 3.4.3. Removing an Item by Value

Sometimes you won’t know the position of the value you want to remove from a list. If you only know the value of the item you want to remove, you can use the ```remove()``` method.

```python
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles) # ['honda', 'yamaha', 'suzuki', 'ducati']

motorcycles.remove('ducati')
print(motorcycles) # ['honda', 'yamaha', 'suzuki']
```

*The ```remove()``` method deletes only the first occurrence of the value you specify. If there’s a possibility the value appears more than once in the list, you’ll need to use a loop to make sure all occurrences of the value are removed.

### 3.5. Organizing a List

#### 3.5.1. Sorting a List Permanently with the sort() Method

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars) # ['audi', 'bmw', 'subaru', 'toyota']
```

You can also sort this list in reverse-alphabetical order by passing the argument ```reverse=True``` to the ```sort()``` method.

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars) # ['toyota', 'subaru', 'bmw', 'audi']
```

#### 3.5.2. Sorting a List Temporarily with the sorted() Function

To maintain the original order of a list but present it in a sorted order, you can use the ```sorted()``` function.

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:") # Here is the original list:
print(cars) # ['bmw', 'audi', 'toyota', 'subaru']

print("\nHere is the sorted list:") # Here is the sorted list:
print(sorted(cars)) # ['audi', 'bmw', 'subaru', 'toyota']

print("\nHere is the original list again:") # Here is the original list again:
print(cars) # ['bmw', 'audi', 'toyota', 'subaru']
```

The sorted() function can also accept a reverse=True argument if you want to display a list in reverse-alphabetical order.

#### 3.5.3. Reverse the original order of a list

To reverse the original order of a list, you can use the ```reverse()``` method.

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars) # ['bmw', 'audi', 'toyota', 'subaru']

cars.reverse()
print(cars) # ['subaru', 'toyota', 'audi', 'bmw']
```

#### 3.5.4. Finding the Length of a List

You can quickly find the length of a list by using the ```len()``` function.

```python
>>> cars = ['bmw', 'audi', 'toyota', 'subaru']
>>> len(cars)
4
```

*Python counts the items in a list starting with one, so you shouldn’t run into any off-by-one errors when determining the length of a list.

Keep in mind that whenever you want to access the last item in a list, you should use the index ```-1```. This will always work, even if your list has changed size since the last time you accessed it:

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[-1]) # suzuki
```

The only time this approach will cause an error is when you request the last item from an empty list.

## 4. WORKING WITH LISTS

### 4.1. Looping Through an Entire List

When you want to do the same action with every item in a list, you can use Python’s for loop.

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    # Alice, that was a great trick!
    # David, that was a great trick!
    # Carolina, that was a great trick!
```

When writing your own for loops that you can choose any name you want for the temporary variable that will be associated with each value in the list. However, it’s helpful to choose a meaningful name that represents a single item from the list.

```python
for cat in cats:
for dog in dogs:
for item in list_of_items:
```

### 4.2. Using the range() Function

Python’s ```range()``` function makes it easy to generate a series of numbers.

```python
for value in range(1, 5):
    print(value)
    # 1
    # 2
    # 3
    # 4
```

#### 4.2.1. Using range() to Make a List of Numbers

If you want to make a list of numbers, you can convert the results of ```range()``` directly into a list using the ```list()``` function.

```python
numbers = list(range(1, 6))
print(numbers) # [1, 2, 3, 4, 5]
```

We can also use the ```range()``` function to tell Python to skip numbers in a given range. If you pass a third argument to ```range()```, Python uses that value as a step size when generating numbers.

```python
even_numbers = list(range(2, 11, 2))
print(even_numbers) # [2, 4, 6, 8, 10]
```

### 4.3. Simple Statistics with a List of Numbers

A few Python functions are helpful when working with lists of numbers. For example, you can easily find the minimum, maximum, and sum of a list of numbers:

```python
>>> digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
>>> min(digits)
0
>>> max(digits)
9
>>> sum(digits)
45
```

### 4.4. List Comprehensions

A list comprehension allows you to generate lists in just one line of code. A list comprehension combines the for loop and the creation of new elements into one line, and automatically appends each new element.

```python
squares = [value**2 for value in range(1, 11)]
print(squares) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

### 4.5. Working with Part of a List

### 4.5.1. Slicing a List

To make a slice, you specify the index of the first and last elements you want to work with. 

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) # ['charles', 'martina', 'michael']
```

If you omit the first index in a slice, Python automatically starts your slice at the beginning of the list:

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4]) # ['charles', 'martina', 'michael', 'florence']
```

A similar syntax works if you want a slice that includes the end of a list.

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:]) # ['michael', 'florence', 'eli']
```

### 4.5.2. Looping Through a Slice

You can use a slice in a for loop if you want to loop through a subset of the elements in a list.

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team:") # Here are the first three players on my team:
for player in players[:3]:
    print(player.title())
    # Charles
    # Martina
    # Michael
```

### 4.5.3. Copying a List

```python
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:") # My favorite foods are:
print(my_foods) # ['pizza', 'falafel', 'carrot cake', 'cannoli']

print("\nMy friend's favorite foods are:") # My friend's favorite foods are:
print(friend_foods) # ['pizza', 'falafel', 'carrot cake', 'ice cream']
```

### 4.6. Tuples

Sometimes you’ll want to create a list of items that cannot change.
Python refers to values that cannot change as immutable, and an immutable list is called a tuple.

#### 4.6.1. Defining a Tuple

A tuple looks just like a list, except you use parentheses instead of square brackets. 

```python
dimensions = (200, 50)
print(dimensions[0]) # 200
print(dimensions[1]) # 50
```

You can loop over all the values in a tuple using a for loop, just as you did with a list.

#### 4.6.2. Writing Over a Tuple

Although you can’t modify a tuple, you can assign a new value to a variable that represents a tuple.

```python
dimensions = (200, 50)
print("Original dimensions:") # Original dimensions:
for dimension in dimensions: # 200
    print(dimension) # 50

dimensions = (400, 100)
print("\nModified dimensions:") # Modified dimensions:
for dimension in dimensions: # 400 
    print(dimension) # 100
```

## 5. IF STATEMENTS

The following example shows how if tests let you respond to special situations correctly.

```python
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
# Audi
# BMW
# Subaru
# Toyota
```

### 5.1. Conditional Tests

#### 5.1.1. Checking for Equality

```python
>>> car = 'bmw'
>>> car == 'bmw'
True
```

#### 5.1.2. Checking for Inequality

```python
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!") 
# Hold the anchovies!
```

#### 5.1.3. Numerical Comparisons

```python
>>> age = 19
>>> age < 21
True
>>> age <= 21
True
>>> age > 21
False
>>> age >= 21
False
```

#### 5.1.4. Using and to Check Multiple Conditions

```python
>>> age_0 = 22
>>> age_1 = 18
>>> age_0 >= 21 and age_1 >= 21
False
>>> age_1 = 22
>>> age_0 >= 21 and age_1 >= 21
True
```

#### 5.1.5. Using or to Check Multiple Conditions

```python
>>> age_0 = 22
>>> age_1 = 18
>>> age_0 >= 21 or age_1 >= 21
True
>>> age_0 = 18
>>> age_0 >= 21 or age_1 >= 21
False
```

### 5.2. Checking Whether a Value Is in a List

To find out whether a particular value is already in a list, use the keyword ```in```.

```python
>>> requested_toppings = ['mushrooms', 'onions', 'pineapple']
>>> 'mushrooms' in requested_toppings
True
>>> 'pepperoni' in requested_toppings
False
```

### 5.3. Checking Whether a Value Is Not in a List

```python
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

# Marie, you can post a response if you wish.
```

### 5.4. Boolean Expressions

A Boolean expression is just another name for a conditional test.

### 5.5. Simple if Statements

```python
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
```

### 5.6. The if-elif-else Chain

```python
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}.")
# Your admission cost is $25.
```

You can use as many elif blocks in your code as you like. 
Python does not require an else block at the end of an if-elif chain.

## 6. DICTIONARIES

### 6.1. A Simple Dictionary

A **dictionary** in Python is a collection of **key-value** pairs.

To get the value associated with a key, give the name of the dictionary and then place the key inside a set of square brackets.

```python
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color']) # green
print(alien_0['points']) # 5
```

### 6.2. Adding New Key-Value Pairs

Dictionaries are dynamic structures, and you can add new key-value pairs to a dictionary at any time. To add a new key-value pair, you would give the name of the dictionary followed by the new key in square brackets, along with the new value.

```python
alien_0 = {'color': 'green', 'points': 5}
print(alien_0) # {'color': 'green', 'points': 5}

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0) # {'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}
```

### 6.3. Modifying Values in a Dictionary

To modify a value in a dictionary, give the name of the dictionary with the key in square brackets and then the new value you want associated with that key.

```python
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.") # The alien is green.

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.") # The alien is now yellow.
```

### 6.4. Removing Key-Value Pairs

When you no longer need a piece of information that’s stored in a dictionary, you can use the ```del``` statement to completely remove a key-value pair. 

```python
alien_0 = {'color': 'green', 'points': 5}
print(alien_0) # {'color': 'green', 'points': 5}

del alien_0['points']
print(alien_0) # {'color': 'green'}
```

### 6.5. Using get() to Access Values

Using keys in square brackets to retrieve the value you’re interested in from a dictionary might cause one potential problem: if the key you ask for doesn’t exist, you’ll get an error.

The get() method requires a key as a first argument. As a second optional argument, you can pass the value to be returned if the key doesn’t exist:

```python
alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value) # No point value assigned.
```

If there’s a chance the key you’re asking for might not exist, consider using the get() method instead of the square bracket notation.

### 6.6. Looping Through a Dictionary

You can loop through all of a dictionary’s key-value pairs, through its keys, or through its values.

```python
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
# Key: username
# Value: efermi

# Key: first
# Value: enrico

# Key: last
# Value: fermi
```

#### 6.6.1. Looping Through All the Keys in a Dictionary

The keys() method is useful when you don’t need to work with all of the values in a dictionary. Let’s loop through the favorite_languages dictionary and print the names of everyone who took the poll:

```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

for name in favorite_languages.keys():
    print(name.title())
# Jen
# Sarah
# Edward
# Phil  
```

Looping through the keys is actually the default behavior when looping through a dictionary, so this code would have exactly the same output if you wrote: ```for name in favorite_languages:```

You can choose to use the keys() method explicitly if it makes your code easier to read, or you can omit it if you wish.

#### 6.6.2. Looping Through All Values in a Dictionary

```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

print("The following languages have been mentioned:") # The following languages have been mentioned:
for language in favorite_languages.values():
    print(language.title())
# Python
# C
# Rust
# Python
```

To see each language chosen without repetition, we can use a ```set()```. A set is a collection in which each item must be unique:

```python
favorite_languages = {
    --snip--
    }

print("The following languages have been mentioned:") # 
for language in set(favorite_languages.values()):
    print(language.title())
# Python
# C
# Rust
```

#### 6.6.3. set()

You can build a set directly using braces and separating the elements with commas:

```python
>>> languages = {'python', 'rust', 'python', 'c'}
>>> languages
{'rust', 'python', 'c'}
```

It’s easy to mistake sets for dictionaries because they’re both wrapped in braces. When you see braces but no key-value pairs, you’re probably looking at a set. Unlike lists and dictionaries, sets do not retain items in any specific order.

### 6.7. Nesting

#### 6.7.1. A List of Dictionaries

```python
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
```

A more realistic example would involve more than three aliens with code that automatically generates each alien. In the following example, we use range() to create a fleet of 30 aliens:

```python
# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")
```

These aliens all have the same characteristics, but Python considers each one a separate object, which allows us to modify each alien individually.

#### 6.7.2. A List in a Dictionary

```python
# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

print(f"\nYou ordered a {pizza['crust']}-crust pizza with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")
```

You should not nest lists and dictionaries too deeply

#### 6.8. A Dictionary in a Dictionary

You can nest a dictionary inside another dictionary, but your code can get complicated quickly when you do. For example, if you have several users for a website, each with a unique username, you can use the usernames as the keys in a dictionary.

```python
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },

    }

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

# Username: aeinstein
#     Full name: Albert Einstein
#     Location: Princeton

# Username: mcurie
#     Full name: Marie Curie
#     Location: Paris
```

Notice that the structure of each user’s dictionary is identical. Although not required by Python, this structure makes nested dictionaries easier to work with. If each user’s dictionary had different keys, the code inside the for loop would be more complicated.

## 7. USER INPUT AND WHILE LOOPS

### 7.1. How the input() Function Works

The input() function pauses your program and waits for the user to enter some text. 

```python
message = input("Tell me something, and I will repeat it back to you: ") # Tell me something, and I will repeat it back to you: Hello everyone!
print(message) # Hello everyone!
```

### 7.1.1 Multiple lines prompt

Sometimes you’ll want to write a prompt that’s longer than one line. For example, you might want to tell the user why you’re asking for certain input. You can assign your prompt to a variable and pass that variable to the input() function. This allows you to build your prompt over several lines, then write a clean input() statement.

```python
prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")
# If you share your name, we can personalize the messages you see.
# What is your first name? Eric

# Hello, Eric!
```

## 7.2. Introducing while Loops

### 7.2.1. The while Loop in Action

```python
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
# 1
# 2
# 3
# 4
# 5
```

### 7.2.2. Letting the User Choose When to Quit

```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

    if message != 'quit':
        print(message)
```

### 7.2.3. Using a Flag

```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
```

### 7.2.4. Using break to Exit a Loop

```python
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
```

### 7.2.5. Using continue in a Loop

```python
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)
# 1
# 3
# 5
# 7
# 9
```

### 7.3. Moving Items from One List to Another

```python
# Start with users that need to be verified,
#  and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
#  Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# Verifying user: Candace
# Verifying user: Brian
# Verifying user: Alice

# The following users have been confirmed:
# Candace
# Brian
# Alice
```

### 7.4. Removing All Instances of Specific Values from a List

```python
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
# ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# ['dog', 'dog', 'goldfish', 'rabbit']
```

### 7.5. Filling a Dictionary with User Input

```python
responses = {}
# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store the response in the dictionary.
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")

# What is your name? Eric
# Which mountain would you like to climb someday? Denali
# Would you like to let another person respond? (yes/ no) yes

# What is your name? Lynn
# Which mountain would you like to climb someday? Devil's Thumb
# Would you like to let another person respond? (yes/ no) no

# --- Poll Results ---
# Eric would like to climb Denali.
# Lynn would like to climb Devil's Thumb.
```