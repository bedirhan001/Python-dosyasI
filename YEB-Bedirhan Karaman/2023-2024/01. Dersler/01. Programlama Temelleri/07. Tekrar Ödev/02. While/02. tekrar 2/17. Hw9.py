toplam = 0
terim_sayısı = 0
reply = True

while reply:
    number = int(input("sayı giriniz (ortalama için 1 e bas) :"))
    
    if number == 1:
        if terim_sayısı != 0:  
            ortalama = toplam / terim_sayısı
            print("ortalama", ortalama)
        else:
            print("Henüz sayı girilmedi.")
        reply = False
    else:
        toplam += number
        terim_sayısı += 1
