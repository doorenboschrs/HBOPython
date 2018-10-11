a = 1
b = 2
som = 0
getallen = 0
while b > a:
    nummer = eval(input("Geef een getal: "))
    som = som + nummer
    getallen = getallen + 1
    if nummer == 0:
        print("Er zijn " + str(getallen-1) + " ingevoerd, de som is: " + str(som))
        break

