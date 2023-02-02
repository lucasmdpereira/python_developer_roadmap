# 4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:

cubes_list = [number**3 for number in range(1,11)]
print(cubes_list)

# Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
number_of_items = 3

first_n_items = cubes_list[:number_of_items]
print("The first three items in the list are:")
print(first_n_items)

# Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.

middle_n_items = cubes_list[number_of_items:number_of_items+3]
print("Three items from the middle of the list are:")
print(middle_n_items)

# Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.

last_n_items = cubes_list[-number_of_items:]
print("Three items from the middle of the list are:")
print(last_n_items)