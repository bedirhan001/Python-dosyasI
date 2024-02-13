kelime = input("Şifre girin: ")

reply = True

while reply:
    if kelime == "python":
        reply = False
    else:
        kelime = input("Yanlış şifre. Tekrar deneyin: ")
