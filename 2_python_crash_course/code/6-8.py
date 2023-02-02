# Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as you do, print everything you know about each pet.

pet1 = {
    "name": "name1",
    "kind": "kind1",
    "owner": "owner1"
}
pet2 = {
    "name": "name2",
    "kind": "kind2",
    "owner": "owner2"
}
pet3 = {
    "name": "name3",
    "kind": "kind3",
    "owner": "owner3"
}

pets = [pet1, pet2, pet3]

for pet in pets:
    print("")
    print(pet["name"])
    for k, v in pet.items():
        if k != "name":
            print(f"{k}: {v}")