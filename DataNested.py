zoo = {
    "Lion": {"Class": "Mammal", "Habitat": "Plains", "Diet": "Carnivore"},
    "Elephant": {"Class": "Mammal", "Habitat": "Plains/Forest", "Diet": "Herbivore"},
    "Pelican": {"Class": "Bird", "Habitat": "Coastal", "Diet": "Carnivore"},
}
print("Pelican's habitat:", zoo["Pelican"]["Habitat"])

zoo["Shark"] = {"Class": "Fish", "Habitat": "Ocean", "Diet": "Carnivore"}
print("Updated zoo", zoo)