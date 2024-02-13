ilk = int(input("İlk sayıyı giriniz: "))
son = int(input("İkinci sayıyı giriniz: "))

toplam = 0
sayı_mik = 0

while ilk <= son:
    toplam += ilk
    sayı_mik += 1
    ilk += 1

ortalama = toplam / sayı_mik
print("Girilen sayıların ortalaması:", ortalama)