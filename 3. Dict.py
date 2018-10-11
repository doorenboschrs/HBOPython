cijferlijst = {"Bob":8, "Lenord":10, "Brad":2, "Jan":1, "Hans":6, "George":9, "Roos":10, "Britney":1 }
studentencijfers = cijferlijst.items()
for student in studentencijfers:
    if student[1] > 9:
        print(student)
