a1 = int(input("ilk açıyı giriniz :"))
a2 = int(input("ikinci açıyı giriniz :"))
a3 = int(input("üçüncü açıyı giriniz :"))

toplam = a1 + a2 + a3 

if toplam == 180 and a1 < 0 and a2 < 0 and a3 <0 : 
    print("bu bir üçgendir ")
else : 
    print("bu bir üçgen değildir ")