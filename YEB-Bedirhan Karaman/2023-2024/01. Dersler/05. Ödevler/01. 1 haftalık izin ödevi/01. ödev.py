bütçe = float(input("Bütçenizi giriniz: "))
toplam_tutar = 0
ürün_adeddi = 0

while True:
    seçim = input("Almak istediğiniz meyveyi seçin:\n"
                  "Elma = 10 TL\n"
                  "Portakal = 15 TL\n"
                  "Çilek = 5 TL\n"
                  "karpuz = 30tl \n"
                  "kiraz = 5 tl \n"
                  "Çıkış ve toplam tutar için 'q' ye basın\n")

    if seçim == "q":
        print("Toplam tutar:", toplam_tutar)
        break
    else:
        if bütçe <= 0:
            print("Paranız yok!")
            break

        if seçim == "elma":
            fiyat = 10
        elif seçim == "portakal":
            fiyat = 15
        elif seçim == "çilek":
            fiyat = 5
        elif seçim == "kiraz" :
            fiyat = 5 
        elif seçim == "karpuz":
            fiyat = 30 
        else:
            print("Geçersiz seçim! Lütfen geçerli bir meyve seçin.")
            continue

        if bütçe < fiyat:
            print("Yetersiz bütçe! Başka bir meyve seçin.")
        else:
            bütçe -= fiyat
            toplam_tutar += fiyat
            print(seçim, "satın alındı. Paranızdan" ,fiyat ,"TL düşüldü. Kalan bütçe:", bütçe,"TL")