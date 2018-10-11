kluisnummer = [1,2,3,4,5,6,7,8,9,10,11,12]
aantalregels = 0
kluisnummerwachtwoord = ""
a = 2
b = 1

def toon_aantal_kluizen_vrij(aantalregels):
    infile = open("kluizen.txt")
    ar = infile.readlines()
    infile.close()
    for regel in ar:
        aantalregels = aantalregels + 1
    if aantalregels > 0:
        print("Er zijn " + str(12 - aantalregels) + " kluizen vrij" + "\n")
    else:
        print("Er zijn 12 kluizen vrij" + "\n")


def nieuwe_kluis(kluisnummer):
    infile2 = open("kluizen.txt")
    gk = infile2.readlines()
    for regel2 in gk:
        for nummer in kluisnummer:
            if str(nummer) in regel2:
                kluisnummer.remove(nummer)
    print(kluisnummer)
    print("De getallen boven deze zin zijn de kluizen die vrij zijn" + "\n")
    if 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10 or 11 or 12 in kluisnummer:
        welkekluisneemtu = eval(input("Welke kluis neemt u? Type hier uw kluis nummer in: "))
        kluiswachtwoord = input("U moet nu een nieuw wachtwoord maken voor de kluis. Type minimaal vier tekens in: ")
        if len(kluiswachtwoord) < 4:
            infile2.close()
            print("Uw wachtwoord is niet sterk genoeg. U wordt nu naar de startmenu verstuurd" + "\n")
        else:
            infile2.close()
            outfile = open("kluizen.txt", "a")
            outfile.write(str(welkekluisneemtu) + ";" + kluiswachtwoord + "\n")
    else:
        print("Er zijn momenteel geen kluizen vrij")


def kluis_openen(kluisnummerwachtwoord):
    kluisnummervragen = eval(input("Wat is uw kluisnummer?: "))
    wachtwoordvragen = input("Wat is uw wachtwoord?: ")
    kluisnummerwachtwoord = str(str(kluisnummervragen) + ";" + wachtwoordvragen)
    infile3 = open("kluizen.txt")
    wachtwoordchecken = infile3.readlines()
    infile3.close()
    for genummerderegels in wachtwoordchecken:
        if kluisnummerwachtwoord in genummerderegels:
            print("De combinatie klopt" + "\n")
        else:
            print("De combinatie is vals" + "\n")



def kluis_teruggeven(kluisnummer, kluisnummerwachtwoord):
    kluisnummerteruggeven = eval(input("Type uw kluis nummer in: "))
    kluiscodeterug = input("type hier uw kluis wachtwoord in: ")
    kluisnummerwachtwoord = str(str(kluisnummerteruggeven) + ";" + kluiscodeterug)
    infile4 = open("kluizen.txt", "r")
    outfile4 = infile4.readlines()
    infile4.close()
    infile4 = open("kluizen.txt", "w")
    for lijn in outfile4:
        if lijn != kluisnummerwachtwoord + "\n":
            infile4.write(lijn)
    print("De kluis is terug gegeven" + "\n")




while a > b:
    menu = eval(input("1: Ik wil weten hoeveel kluizen nog vrij zijn" + "\n" + "\n" + "2: Ik wil een nieuwe kluis" + "\n" + "3: Ik wil even iets uit mijn kluis halen" + "\n" + "4: Ik geef mijn kluis terug" + "\n" + "5: Ik wil stoppen" + "\n"))
    if menu == int(1):
        toon_aantal_kluizen_vrij(aantalregels)
    elif menu == int(2):
        nieuwe_kluis(kluisnummer)
    elif menu == int(3):
        kluis_openen(kluisnummerwachtwoord)
    elif menu == int(4):
        kluis_teruggeven(kluisnummer, kluisnummerwachtwoord)
    elif menu == int(5):
        a = 0
    else: menu

