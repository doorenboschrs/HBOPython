a = 1
b = 2

while b > a:
    word = input("Geen een string van vier letters: ")
    if len(word) == 4:
        print("Inlezen van correcte string: " + word + " is geslaagd")
        break
    else:
        print(word + " heeft " + str(len(word)) + " letters")
