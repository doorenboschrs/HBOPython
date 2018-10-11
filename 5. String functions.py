aantal = 0
lengte = 0

def gemiddelde(aantal, lengte):
    will = input("Voer hier een willikeurige zin in: ")
    willekeurig = will.split()
    for woord in willekeurig:
        aantal = aantal + 1
        lengte = lengte + len(woord)
    print(lengte / aantal)

gemiddelde(aantal, lengte)
