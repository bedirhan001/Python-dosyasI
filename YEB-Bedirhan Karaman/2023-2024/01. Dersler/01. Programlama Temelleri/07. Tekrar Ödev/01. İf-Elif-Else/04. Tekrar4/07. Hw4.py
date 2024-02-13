fiyat1 = int(input("birinci fiyatı giriniz :"))
fiyat2 = int(input("ikinci fiyatı giriniz :"))

toplam = fiyat1 + fiyat2
indiirm = toplam -(toplam * 0.25)

if toplam <= 200 :
    print("fiyat :",toplam)
elif toplam > 200 :
    print("fiyat:",indiirm)