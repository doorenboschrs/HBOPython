invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
totaal = 0

lijst = invoer.split("-")
lijst.sort()

for getal in lijst:
    totaal = int(totaal) + int(getal)

print("Gesorteerde list van ints: " + str(lijst))
print("Grootste getal: " + str(lijst[-1]) + " en Kleinste getal: " + str(lijst[0]))
print("Aantal getallen: " + str(len(lijst)) + " en Som van de getallen: " + str(totaal))
print("Gemiddelde: " + str((totaal/len(lijst))))
