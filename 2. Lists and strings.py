lijst = eval(input("Geef lijst met minimaal 10 strings: "))
vier = []

for item in lijst:
    if len(item) == 4:
        vier.append(item)
print(vier)
