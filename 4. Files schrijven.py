while 2>1:
    outfile = open("hardlopers.txt", "a")
    naam = input("Schrijf hier de naam van de hardloper: ")
    import datetime
    vandaag = datetime.datetime.today()
    s = vandaag.strftime("%a %d %b %Y, %H:%M:%S, ")
    outfile.write(s + naam + '\n')
    outfile.close()
