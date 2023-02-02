# Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary. Print each person’s name and their favorite number. For even more fun, poll a few friends and get some actual data for your program.

people_favorite_numbers = {
    "person1": 1,
    "person2": 2,
    "person3": 3,
    "person4": 4,
    "person5": 5    
}

for person in people_favorite_numbers:
    print(f"{person}: {people_favorite_numbers[person]} ")
    
    