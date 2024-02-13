ilk = int(input("başlangıç için sayıyı giriniz: \n"))
son = int(input("son sayıyı girin:\n "))
toplam = 0 
terim_sayısı = 0

 
while ilk <= son:
    toplam += ilk
    terim_sayısı += 1
    ilk += 1
ortalama = toplam / terim_sayısı
print("ortalama :",ortalama)