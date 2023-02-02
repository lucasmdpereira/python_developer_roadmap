# People: Start with the program you wrote for Exercise 6-1 (page 98). Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person.

personal_info_1 = {
    "first_name": "person_1_first_name",
    "last_name": "person_1_last_name",
    "age": "person_1_age",
    "city": "person_1_city"
}

personal_info_2 = {
    "first_name": "person_2_first_name",
    "last_name": "person_2_last_name",
    "age": "person_2_age",
    "city": "person_2_city"
}

people = [personal_info_1, personal_info_2]

print("")
for person in people:
    for k, v in person.items():
        print(f"{k}, {v}")
    print("")