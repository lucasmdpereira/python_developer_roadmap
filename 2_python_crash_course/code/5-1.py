# Conditional Tests: Write a series of conditional tests. Print a statement describing each test and your prediction for the results of each test. Your code should look something like this:

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

# Look closely at your results, and make sure you understand why each line evaluates to True or False.
# Create at least 10 tests. Have at least 5 tests evaluate to True and another 5 tests evaluate to False.

number = 42
#1
print("\nIs number == 42? I predict True.")
print(number == 42)

#2
print("\nIs number == 10? I predict False.")
print(number == 10)

is_true = True
#3
print("\nIs is_true == True? I predict True.")
print(is_true == True)

#4
print("\nIs is_true == False? I predict False.")
print(is_true == False)

is_true = True
#5
print("\nIs is_true type == boolean? I predict True.")
print(type(is_true) == type(True))

#6
print("\nIs is_true type == string? I predict True.")
print(type(is_true) == type("string"))

name = "Ana"
#7
print("\nThe first letter of name == 'a'? I predict True.")
print(name[0].lower() == 'a')

#8
print("\nThe first letter of name == 'b'? I predict False.")
print(name[0].lower() == 'b')

array = range(1,11)
#9
print("\nDoes the array have 10 elements? I predict True.")
print(len(array) == 10)

#10
print("\nDoes the array have 20 elements? I predict True.")
print(len(array) == 20)
