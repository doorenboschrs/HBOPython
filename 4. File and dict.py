outfile = open("bedrijven.txt", "w")
outfile.write("YAHOO:YHOO" + "\n" + "GOOGLE INC:GOOG" + "\n" + "Harley-Davidson:HOG" + "\n" + "Yamana Gold:AUY" + "\n" + "Sotheby's:BID" + "\n" + "inBev:BUD")
outfile.close()

filename = {}

def ticker(filename):
    bedrijfnaam = input("Enter Company name: ")

    outfile = open("bedrijven.txt", "r")
    infile = outfile.readlines()
    outfile.close()
    for lijn in infile:
        if bedrijfnaam in lijn:
            gesplits = lijn.split(":")
            eerste = gesplits[0]
            tweede = gesplits[1].replace("\n", "")
            new ={eerste:tweede}
            print("Ticker symbol: " + tweede + "\n")
            filename.update(new)
            return filename


def symbol(filename):
    ticker(filename)
    tickersymbol = input("Enter Ticker symbol: ")

    outfile = open("bedrijven.txt", "r")
    infile = outfile.readlines()
    outfile.close()
    for lijn in infile:
        if tickersymbol in lijn:
            gesplits = lijn.split(":")
            eerste = gesplits[0]
            tweede = gesplits[1].replace("\n", "")
            new ={eerste:tweede}
            print("Company name: " + eerste)
            filename.update(new)







symbol(filename)
