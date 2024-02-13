number = [35, 26, 81, 64]

number.sort(reverse=True)

ters_sayilar = number[::-1]

sayi_26_adeti = number.count(26)

number.remove(81)


sayilar = [35, 26, 81, 64]
sayilar.sort(reverse=True)
print("Büyükten küçüğe sıralanmış liste:", sayilar)

ters_sayilar = sayilar[::-1]
print("Listenin ters hali:", ters_sayilar)

sayi_26_adeti = sayilar.count(26)
print("Listede 26 elemanının adeti:", sayi_26_adeti)

sayilar.remove(81)
print("81 sayısı silindi. Yeni liste:", sayilar)

sayilar.clear()
print("Liste tüm elemanlarıyla birlikte boşaltıldı")