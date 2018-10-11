afstandKM = eval(input("Kilometer gereden: "))
leeftijd = eval(input("Wat is uw leeftijd?: "))
weekendrit = input("Welke dag rijd jij(type in kleine letters)?: ")



def standaardprijs(afstandKM):
    if afstandKM <= 0:
        print("De standaard prijs kost 0,00 euro")
        return afstandKM
    elif afstandKM >= 50:
        print("De De standaard prijs kost " + str((afstandKM * 0.60)+15) + "euro")
        return afstandKM
    else:
        print("De De standaard prijs kost " + str(0.80 * afstandKM) + " euro")
        return afstandKM

def ritprijs(leeftijd, weekendrit, afstandKM):
    standaardprijs(afstandKM)

    prijs = 0

    if afstandKM == 0:
        prijs = 0
    elif afstandKM >= 50:
        prijs = (afstandKM * 0.60) + 15
    else:
        prijs = afstandKM * 0.80

    if leeftijd >= 65 or 12 >= leeftijd:
        if weekendrit == "zaterdag" or "zondag":
            print("Uw momentele kosten zijn " + str((prijs / 100) * 65) + "euro")
        else:
            print("Uw momentele kosten zijn " + str((prijs / 100) * 70) + "euro")
    else:
        if weekendrit == "zaterdag" or "zondag":
            print("Uw momentele kosten zijn " + str((prijs / 100) * 60) + "euro")
        else:
            print("Uw momentele kosten zijn " + str(prijs) + "euro")


ritprijs(leeftijd, weekendrit, afstandKM)
