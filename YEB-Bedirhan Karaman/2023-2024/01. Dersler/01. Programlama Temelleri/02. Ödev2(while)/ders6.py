baslangic = int(input("ilk sayıyı giriniz: "))
bitis = int(input("ikinci sayıyı giriniz: "))

toplam = 0

while baslangic <= bitis:
    toplam += baslangic
    baslangic += 1

print("sayıların toplamı :", toplam)