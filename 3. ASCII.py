invoerstring = input("Voer hier uw naam, beginstation en eindstation achter elkaar in: ")
def code(invoerstring):
    for letter in invoerstring:
        test = chr(ord(letter) + 3)
        print(test, end= "")




code(invoerstring)
