infile = open("kaartnummers.txt")
regels = infile.readlines()
infile.close()

print("Deze file telt " + str(len(regels)) + " regels")

groot = 0
rl = 1

for line in regels:
    r = line.split(",")
    if int(r[0]) >= groot:
        groot = int(r[0])
        rl = rl + 1


print("Het grootste kaarnummer is: " + str(groot) + " en dat staat op regel " + str(rl))
