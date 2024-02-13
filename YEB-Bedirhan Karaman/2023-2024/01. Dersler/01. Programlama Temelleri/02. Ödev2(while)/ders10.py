dogru_sifre = "python"
sifre = input("Şifre giriniz: ")

while sifre != dogru_sifre:
    print("Hatalı şifre! Tekrar deneyin.")
    sifre = input("Şifre giriniz: ")

print("Doğru şifre girdiniz. Hoş geldiniz!")
