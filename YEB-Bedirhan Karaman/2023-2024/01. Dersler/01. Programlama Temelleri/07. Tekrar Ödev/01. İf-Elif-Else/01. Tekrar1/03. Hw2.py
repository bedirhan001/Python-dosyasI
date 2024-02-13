angle1 = int(input("birinci açıyı giriniz: "))
angle2 = int(input("ikinci açıyı giriniz: "))
angle3 = int(input("üçüncü açıyı giriniz: "))

toplam = angle1 + angle2 + angle3 

if toplam == 180 and angle1 < 0 and angle2 < 0 and angle3 < 0 : 
    print("bu bir üçgendir ")
else : 
    print("bu bir üçgendir ")