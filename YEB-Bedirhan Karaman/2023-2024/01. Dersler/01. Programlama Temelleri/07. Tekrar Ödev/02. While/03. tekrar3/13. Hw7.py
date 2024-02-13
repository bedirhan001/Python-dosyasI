n1 = int(input("ilk sayıyı gir :"))
n2 = int(input("ikinci sayıyı gir :"))

toplam = 0 
terim_sayısı = 0

while n1 <= n2 :
    toplam += n1 
    terim_sayısı += 1
    n1 += 1

ortalama = toplam/terim_sayısı
print(ortalama)
