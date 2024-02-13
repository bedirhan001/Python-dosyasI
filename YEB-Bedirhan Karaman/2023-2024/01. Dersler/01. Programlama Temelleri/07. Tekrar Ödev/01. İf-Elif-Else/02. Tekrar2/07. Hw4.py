urun1 = float(input("Birinci ürünün fiyatını girin: "))
urun2 = float(input("İkinci ürünün fiyatını girin: "))

toplam = urun1 + urun2
indirim = toplam * 0.25
sonra = toplam - indirim  

if toplam > 20 : 
    print("ödenecek tutar indirimden sonra :",sonra)
else :
    print("ücret gerekli değil")  