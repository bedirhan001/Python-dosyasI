toplam = 0
miktar = 0
devam_et = True

while devam_et:
    sayi = int(input("Bir sayı girin (1 girmek için çıkış yapın): "))

    if sayi == 1:
        print("Çıkış yapılıyor.")
        devam_et = False
    else:
        toplam += sayi
        miktar += 1

if miktar > 0:
    ortalama = toplam / miktar
    print("Girilen sayıların ortalaması:", ortalama)
else:
    print("Hiç sayı girilmedi.")
