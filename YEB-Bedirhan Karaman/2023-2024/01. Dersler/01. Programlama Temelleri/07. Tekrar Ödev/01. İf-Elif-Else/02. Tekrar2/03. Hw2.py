açı1 = int(input("ilk açıyı giriniz :"))
açı2 = int(input("ikinci açıyı giriniz :"))
açı3 = int(input("üçüncü açıyı giriniz :"))

toplam = açı1 + açı2 + açı3 

if toplam == 180 and açı1 < 0 and açı2 < 0 and açı3 <0 : 
    print("bu bir üçgendir ")
else : 
    print("bu bir üçgen değildir ")