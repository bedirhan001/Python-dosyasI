sayilar = [35, 26, 81, 64]

sayilar.sort(reverse=True)
print("a) Büyükten küçüğe sıralı liste:", sayilar)

sayilar_tersten = sayilar[::-1]
print("b) Listenin tersten yazılmış hali:", sayilar_tersten)

adet_26 = sayilar.count(26)
print("c) Listedeki 26 sayısının adedi:", adet_26)

sayilar.remove(81)
print("ç) 81 sayısı silindi. Yeni liste:", sayilar)

sayilar.clear()
print("d) Liste tamamen boşaltıldı. Yeni liste:", sayilar)
