def şifreal():
    return input("şifre gir: \n")

def şifrekaçharfli(password):
    if len(password) != 8:
        print("şifre 8 haneli olmalı")
        return False
    return True

password = şifreal()

if şifrekaçharfli(password):
    print("şifre kaydedildi")