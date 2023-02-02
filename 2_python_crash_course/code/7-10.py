# Dream Vacation: Write a program that polls users about their dream vacation. Write a prompt similar to If you could visit one place in the world, where would you go? Include a block of code that prints the results of the poll.

results = {}

while True:
    
    name = input("Name: ")
    place = input("Place: ")
    
    results[name] = place
    
    repeat = input("Another person? (:q for finish) ")
    if repeat == ":q":
        break
    else:
        continue

print(results)