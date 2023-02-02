# 6-5. Rivers: Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.

rivers = {}

number_of_terms = 10
for i in range(0,number_of_terms):
    rivers[f"river{i}"] = f"country{i}"
    
# Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
for k, v in rivers.items():
    print(f"The {k} runs through {v}")
print("")

# Use a loop to print the name of each river included in the dictionary.
for river in sorted(set(rivers.keys())):
    print(river)
print("")

# Use a loop to print the name of each country included in the dictionary.
for country in sorted(set(rivers.values())):
    print(country)
print("")