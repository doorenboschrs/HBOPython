
stations = ["Schagen", "Heerhugowaard", "Alkmaar", "Castricum", "Zaandam", "Amsterdam Sloterdijk", "Amsterdam Centraal", "Amsterdam Amstel", "Utrecht Centraal", "’s-Hertogenbosch", "Eindhoven", "Weert", "Roermond", "Sittard", "Maastricht"]

def inlezen_beginstation(stations):
    bs = input("Type hier uw beginstation in: ")
    if bs in stations:
        return bs
    else:
        print("De station komt niet in onze database voor. Type een ander station in.")
        inlezen_beginstation(stations)

beginstation = inlezen_beginstation(stations)

def inlezen_eindstation(stations, beginstation):
    es = input("Type hier uw eindstation in: ")


