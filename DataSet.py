farm_animals = {"Cow", "Chicken", "Sheep"}
farm_animals.update(["Duck", "Goat"])
wild_animals = {"Lion", "Tiger", "Bear"}
print("Animals:", farm_animals.union(wild_animals))
print("Is Cow in wild animals:", "cow" in  wild_animals)
