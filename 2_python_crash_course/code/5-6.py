# 5-6. Stages of Life: Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:

age = 35

# If the person is less than 2 years old, print a message that the person is a baby.
if age < 2:
    print("You are a baby")
# If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
if age >= 2 and age < 4:
    print("You are a toddler")
# If the person is at least 4 years old but less than 13, print a message that the person is a kid.
if age >= 4 and age < 13:
    print("You are a kid")
# If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
if age >= 13 and age < 20:
    print("You are a teenager")
# If the person is at least 20 years old but less than 65, print a message that the person is an adult.
if age >= 20 and age < 65:
    print("You are an adult")
# If the person is age 65 or older, print a message that the person is an elder.
if age >= 65:
    print("You are an elder")