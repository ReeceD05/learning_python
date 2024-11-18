Wildlife = ["Deer", "Bear", "Wolf", "Badger","Water Vole", "Squirrel"]
print("Original list:", Wildlife)

Wildlife.extend(["Toad", "Crow"])
print("After Extending:", Wildlife)

Wildlife.remove("Wolf")
Wildlife.insert(2, "Penguin")
print("Replace Wolf with Penguin:", Wildlife)

Wildlife.remove("Crow")
print("Removed Crow:", Wildlife)

Wildlife.sort()
print("Alphabetical List", Wildlife)
print("Count of 'Elephant':", Wildlife.count("Elephant"))
