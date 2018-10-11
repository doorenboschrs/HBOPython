grondgetallen = [4, 5, 3, -81]

def kwadraten_som(grondgetallen):
    lijsten = 0
    for nummer in grondgetallen:
        if nummer >= 0:
            lijsten = lijsten + (nummer ** 2)
    return lijsten



kwadraten_som(grondgetallen)
