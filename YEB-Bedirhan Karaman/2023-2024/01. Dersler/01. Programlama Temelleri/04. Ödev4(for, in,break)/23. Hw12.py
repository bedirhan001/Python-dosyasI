while True:
    kelime = input("8 karakterli bir karakter giriniz: ")
    if len(kelime) == 8:
        print("Giriş başarılı, şifre kaydedildi.")
        break
    else:
        print(" 8 karakterli bir şifre girmelisiniz. Tekrar deneyin.")