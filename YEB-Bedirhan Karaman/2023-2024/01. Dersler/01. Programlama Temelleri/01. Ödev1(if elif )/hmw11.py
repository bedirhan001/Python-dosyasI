açı1 = float(input("birinci açıyı giriniz :"))
açı2 = float(input("ikinci açıyı giriniz :"))
açı3 = float(input("üçüncü açıyı giriniz :"))

if açı1 == açı2 == açı3 :
    print("bu bir  eşkenar üçgen ")
elif açı1 == açı2 or açı1 == açı3 or açı2 == açı3 :
    print("bu bir ikizkenar üçgen")
else :
    print("bu bir çeşit kenar üçgendir")