studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]

def gemiddelde_per_student(studentencijfers):
    antw = []
    a = sum(studentencijfers[0])
    b = sum(studentencijfers[1])
    c = sum(studentencijfers[2])
    d = sum(studentencijfers[3])

    ga = a/3
    gb = b/3
    gc = c/3
    gd = d/3

    antw.append(ga)
    antw.append(gb)
    antw.append(gc)
    antw.append(gd)

    return antw


def gemiddelde_van_alle_studenten(studentencijfers):
    eg = (sum(studentencijfers[0])) / 3
    tg = (sum(studentencijfers[1])) / 3
    dg = (sum(studentencijfers[2])) / 3
    vg = (sum(studentencijfers[3])) / 3
    antw = (eg + tg + dg + vg) / 4

    return int(antw)

print(gemiddelde_per_student(studentencijfers))

print(gemiddelde_van_alle_studenten(studentencijfers))
