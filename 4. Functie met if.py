newpassword = input("Type in your new password: ")
oldpassword = "password123"

def checkpassword(newpassword, oldpassword):
    if len(newpassword) >= 6 and newpassword != oldpassword:
        return True
    else:
        return False

checkpassword(newpassword, oldpassword)
