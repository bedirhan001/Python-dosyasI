ağırlık = float(input("Ağırlığınızı kilogram cinsinden giriniz: "))
boy = float(input("Boyunuzu metre cinsinden giriniz: "))

VKİ = ağırlık / (boy * boy) 

if 18 <= VKİ < 25:
    print("Normal kilodasınız.")
elif 25 <= VKİ < 30:
    print("Kilolusunuz.")
elif VKİ >= 35:
    print("Obezsiniz.")
else:
    print("Vücut Kitle İndeksi hesaplanamadı.")