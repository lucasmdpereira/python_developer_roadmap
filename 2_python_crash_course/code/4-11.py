# Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to print out the name of each animal.

animals = ["dog", "cat", "fish", "bird", "rabit"]

print("")
for animal in animals:
    print(animal.title())
    
# Modify your program to print a statement about each animal, such as A dog would make a great pet.

print("")
for animal in animals:
    print(f"{animal.title()} is a good pet!")
    

# Add a line at the end of your program, stating what these animals have in common. You could print a sentence, such as Any of these animals would make a great pet!
print("")  
print("All this animals are good pets!")