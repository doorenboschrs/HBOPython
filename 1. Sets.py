groen = set(["Best", "Beukenlaan", "Geldrop", "Heeze", "Weert"])
bruin = set(["Best", "Beukenlaan", "Helmond 't hout", "Helmond", "Helmond Brouwhuis"])

print(groen.intersection(bruin))
print(bruin.difference(groen))
print(groen.union(bruin))
