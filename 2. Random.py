infile = open("dobelstenengooi.txt", "a")
infile.write("line1" + "\n" + "line2" + "\n" + "line3" + "\n")
infile.close()

def monopolyworp():
    import random
    eerstdoppel = random.randrange(1, 7)
    tweededoppel = random.randrange(1, 7)
    som = eerstdoppel + tweededoppel

    infile = open("dobelstenengooi.txt", "r")
    file = infile.readlines()
    infile.close()
    if "dobbel" == 3 in file:
        print("gevangenis")
    else:
        if eerstdoppel == tweededoppel:
            dubbel = print(str(eerstdoppel) + " + " + str(tweededoppel) + " = " + str(som) + " (dubbel)")
            infile = open("dobelstenengooi.txt", "a+")
            infile.write("dobbel" + "\n")
            infile.close()

        else:
            eerste = print(str(eerstdoppel) + " + " + str(tweededoppel) + " = " + str(som))
            infile = open("dobelstenengooi.txt","w")
            infile.write("line1" + "\n" + "line2" + "\n" + "line3" + "\n")
            infile.close()






monopolyworp()
