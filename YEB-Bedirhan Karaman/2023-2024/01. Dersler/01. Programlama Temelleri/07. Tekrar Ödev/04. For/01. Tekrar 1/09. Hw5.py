x = int(input("ilk sayıyı gir : "))
y = int(input("son sayıyı gir : "))

toplam = 0

for sayı in range(x , y ) :
    toplam += sayı 
print("sayı ",x,"sayı",y,"arasındaki sayıların toplamı :",toplam)