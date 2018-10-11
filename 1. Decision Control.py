maand = eval(input("Schrijf hier de maannummer: "))

def seizoen(maand):
    if maand >= 3 and maand <= 5:
        print("Het is lengte.")
        return "lengte"
    elif maand >= 9 and maand <= 11:
        print("Het is herfst.")
        return "herfst"
    elif maand == 1 or maand == 2 or maand == 12:
        print("Het is winter.")
        return "winter"
    elif maand >= 6 and maand <= 8:
        print("Het is zomer.")
        return "zomer"

seizoen(maand)
