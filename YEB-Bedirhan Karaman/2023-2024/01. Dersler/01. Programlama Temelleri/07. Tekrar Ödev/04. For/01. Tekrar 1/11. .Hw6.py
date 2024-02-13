x = int(input("bir sayı gir : "))
y = int(input("son sayyı gir : "))

toplam = 0 
rakam_sayısı = 0 

for sayı in range (x , y ) :
    toplam += sayı 
    rakam_sayısı += 1 
ortalama = toplam / rakam_sayısı 
print("sayı",x,"ile sayı ",y,"arasındaki sayıların ortalaması",ortalama)
