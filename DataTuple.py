Amphibians = ("Frog", "Axolotl", "Salamander")
print("Second Amphibian:", Amphibians[1])

Amphibians_list = list(Amphibians)
Amphibians_list.append("Newt")
Amphibians = tuple(Amphibians_list)
print("Updated Tuple:", Amphibians)