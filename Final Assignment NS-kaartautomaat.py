
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
    beginstation
    es = input("Type hier uw eindstation in: ")
    if es in stations:
        if  stations.index(es) >= stations.index(beginstation):
            return es
        else:
            print("Error! Type een ander station in.")
            inlezen_eindstation(stations, beginstation)

    else:
        print("Error! Type een ander station in.")
        inlezen_eindstation(stations, beginstation)


eindstation = inlezen_eindstation(stations, beginstation)


def omroepen_reis(stations, beginstation, eindstation):
    beginstation
    eindstation
    print("Het beginstation " + beginstation + " is het " + str(stations.index(beginstation)+1) + "e station in het traject.")
    print("Het eindstation " + eindstation + " is het " + str(stations.index(eindstation)+1) + "e station in het traject.")
    print("De afstand bedraagt " + str(stations.index(eindstation) - stations.index(beginstation)) + " stations(s).")
    print("De prijs van het kaartje is " + str((stations.index(eindstation) - stations.index(beginstation)) * 5) + " euro." + "\n")
    print("Jij stapt in: " + beginstation)
    for s in stations:
        if stations.index(s) > stations.index(beginstation) and stations.index(eindstation) > stations.index(s):
            print("- " + s)
    print("Jij tapt uit in: " + eindstation)

omroepen_reis(stations, beginstation, eindstation)

