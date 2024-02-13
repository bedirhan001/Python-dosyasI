a1 = int(input("birinci açıyı giriniz :"))
a2 = int(input("ikinci açıyı giriniz :"))
a3 = int(input("üçüncü açıyı giriniz :"))

toplam = a1 + a2 + a3

if toplam == 180 :
    if a1 == a2 == a3 :
        print("bu bir eşkenar üçgendir")
    elif a1 == a2 or a1 == a3 or a2 == a3 :
        print("bu bir ikix-zkenar üçgendir ")
    else : 
        print("bu bir çeşitkenar üçgendir")
elif toplam != 180 :
    print("bu bir üçgen değildir")