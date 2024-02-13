birinci_ürün = float(input("İlk ürünün fiyatını girin: "))

urun2_fiyat = float(input("İkinci ürünün fiyatını girin: "))

toplam = birinci_ürün + urun2_fiyat

if toplam <= 200:
    print(f"Ödenecek miktar = {toplam} TL")
else:
    indirimli_fiyat = toplam * 0.75
    print(f"Ödenecek miktar, indirimden sonra {indirimli_fiyat} TL'dir.")