# Favorite Places: Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. Loop through the dictionary, and print each person’s name and their favorite places.

favorite_places = {
    "name1": ["place1", "place2", "place3"],
    "name2": ["place4", "place5", "place6"],
    "name3": ["place7", "place8", "place9"],
}

for name, places in favorite_places.items():
    print("")
    print(f"{name}", end = ": ")
    for place in places:
        print(place, end = ", ")   
print("")