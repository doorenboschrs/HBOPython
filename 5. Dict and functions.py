nietlijst = {}
nummer = 0

def namen(nietlijst, nummer):
    a = 2
    b = 1
    while a > b :
        naam = input("Volgende naam: ")


        if naam == "":
            for i in nietlijst:
                print("Er zijn " + str(nummer) + " studenten met de naam " + naam)
                a = 0
                break




        elif naam in nietlijst:
            nummer = nummer + 1
            nietlijst[naam] = nummer
            namen(nietlijst, nummer)



        else:
            nietlijst[naam] = 1
            namen(nietlijst, nummer)










namen(nietlijst, nummer)
