Habitat = {
    "Forest": ["Deer","Squirrel", "Bat"],
    "Desert": ["Camel", "Meerlat", "Scorpion"],
    "Ocean": ["Shark", "Tuna", "Whale"],
}
print("Habitats:", Habitat)

Habitat["Plains"] = ["Lion", "Zebra", "Elephant"]
print("Updated Habitats", Habitat)

print("Forest:", Habitat["Forest"])

Habitat.pop("Desert")
print("Removed Desert:", Habitat)

print("Habitats:",Habitat.keys())
print("All Animals:", Habitat.values())