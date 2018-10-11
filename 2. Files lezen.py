openfile = open("kaartnummers.txt")
infile = openfile.readlines()
openfile.close()

for line in infile:
    r = line.split(",")
    print(r[1].strip() + " heeft kaartnummer: " + r[0])
