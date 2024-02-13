print("Yeb Restoranına Hoş Geldiniz \n \n \n")

fiyat = 0
sipariş_adedi = 0

while True:
    siparis = input("\n\n\nSipariş vermek istiyor musunuz? (E-e/H-h):\n\n\n\n\n\n ")

    if siparis.upper() == "H":
        if sipariş_adedi < 3:
            print(" \nToplam Fiyat:", fiyat)
        elif sipariş_adedi >= 3:
            indirim = fiyat * 0.15
            indirimli_fiyat = fiyat - indirim
            print("Normal Fiyat:", fiyat, "İndirimli Fiyat:", indirimli_fiyat)
        break

    elif siparis.upper() == "E":
        siparis_2 = input(" \n\n\n Ne sipariş edeceksiniz?\n \n \n "
                          "1: Ana yemekler\n\n\n \n \n "
                          "2: Çorbalar\n \n \n "
                          "3: Tatlılar\n \n \n "
                          "4: Salatalar\n \n \n "
                          "5: İçecekler \n \n \n ")

        if siparis_2 == "1":
            yemek = input("\n \n \nHangi yemeği seçeceksiniz?\n \n \n "
                          "\n \n \n1: Pilav - 30 TL\n \n \n "
                          "\n \n \n2: Köfte - 15 TL\n \n \n "
                          "\n \n \n3: Musakka - 50 TL\n \n \n ")

            if yemek == "1":
                pilav_turu = input("Pilav türünü seçiniz:\n \n \n "
                                   "\n \n \n1: Nohutlu Pilav - 35\n \n \n "
                                   "2: Kuru Fasulyeli Pilav - 40\n \n \n "
                                   "3: Sade Pilav - 30\n \n \n ")
            
                if pilav_turu == "1": 
                    adet = int(input("\n \n \nkaç adet istersiniz : \n \n \n"))                  
                    fiyat += 35 * adet
                    
                elif pilav_turu == "2":  
                    adet = int(input("\n \n \nkaç adet istersiniz : \n \n \n"))                
                    fiyat += 40 * adet

                elif pilav_turu == "3":
                    adet = int(input("\n \n \nkaç adet istersiniz : \n \n \n"))
                    fiyat += 30 * adet

                else:
                    print("\n \n \nGeçersiz pilav türü seçimi.\n \n \n")
        
            elif yemek == "2":
                adet = int(input("\n \n \nkaç adet istersiniz : \n \n \n"))               
                fiyat += 15 * adet

            elif yemek == "3":
                adet = int(input("\n \n \nkaç adet istersiniz : \n \n \n"))
                fiyat += 50 * adet

            else:
                print("\n \n \nHatalı sayı, düzgün bir sayı girin.\n \n \n")

            sipariş_adedi += adet
            print("Siparişiniz alındı:", yemek)
        elif siparis_2 == "3":
            tatlı = input("\n \n \nHangi tatlıyı seçeceksiniz?\n \n \n "
                           "\n \n \n1: Baklava - 25 TL\n \n \n "
                           "\n \n \n2: Traliçe - 10 TL\n \n \n "
                           "\n \n \n3: Kazandibi - 15 TL\n \n \n ")
            dilim_sayisi = int(input("\n \n \nKaç dilim Baklava istersiniz? (normalde: 5): \n \n \n"))
            if tatlı == "1":
                fiyat += 25 * dilim_sayisi

            elif tatlı == "2":       
                fiyat += 10 * dilim_sayisi

            elif tatlı == "3":
                fiyat += 15 * dilim_sayisi

            else:
                print("\n \n \nHatalı sayı, düzgün bir sayı girin.\n \n \n")

            sipariş_adedi += 1
            print("Siparişiniz alındı:", tatlı)
        elif siparis_2 == "2":
            çorba = input("\n \n \nHangi çorbayı seçeceksiniz?\n \n \n "
                           "\n \n \n1: Mercimek Çorbası - 15 TL\n \n \n"
                           "\n \n \n2: Ezogelin Çorbası - 20 TL\n \n \n "
                           "\n \n \n3: Yayla Çorbası - 20 TL\n \n \n")
            adet = int(input("\n \n \nkaç adet istersiniz : \n \n \n"))

            if çorba == "1":
                fiyat += 15 * adet
            elif çorba == "2":
                fiyat += 20 * adet
            elif çorba == "3":
                fiyat += 20 * adet
            else:
                print("\n \n \nHatalı sayı, düzgün bir sayı girin.\n \n \n")

            sipariş_adedi += 1
            print("\n \n \nSiparişiniz alındı:", çorba,"\n \n \n")

        elif siparis_2 == "3":
            tatlı = input("\n \n \nHangi tatlıyı seçeceksiniz?\n \n \n"
                           "\n \n \n1: Baklava - 25 TL\n \n \n "
                           "\n \n \n2: Traliçe - 10 TL\n \n \n "
                           "\n \n \n3: Kazandibi - 15 TL\n \n \n")

            if tatlı == "1":
                dilim_sayisi = int(input("\n \n \nKaç dilim  istersiniz? (normalde: 5): \n \n \n"))
                fiyat += 25 * dilim_sayisi
            elif tatlı == "2":
                dilim_sayisi = int(input("\n \n \nKaç dilim  istersiniz? (normalde: 5): \n \n \n"))
                fiyat += 10 * dilim_sayisi
            elif tatlı == "3":
                dilim_sayisi = int(input("\n \n \nKaç dilim  istersiniz? (normalde: 5): \n \n \n"))
                fiyat += 15 * dilim_sayisi
            else:
                print("\n \n \nHatalı sayı, düzgün bir sayı girin.\n \n \n")

            sipariş_adedi += adet
            print("\n \n \nSiparişiniz alındı:", tatlı,"\n \n \n")

        elif siparis_2 == "4":
            salata = input("\n \n \nHangi salatayı seçeceksiniz?\n \n \n "
                            "\n \n \n1: Rus Salatası - 20 TL\n \n \n "
                            "\n \n \n: Sezar Salatası - 10 TL\n \n \n "
                            "\n \n \n3: Tavuklu Salata - 30 TL\n \n \n ")
            adet = int(input("\n \n \nkaç adet istersiniz: \n \n \n"))
            if salata == "1":
                fiyat += 20 * adet

            elif salata == "2":
                fiyat += 10 * adet

            elif salata == "3":
                fiyat += 30 *  adet

            else:
                print("\n \n \nHatalı sayı, düzgün bir sayı girin.\n \n \n")

            sipariş_adedi += adet
            print("Siparişiniz alındı:", salata)
        elif siparis_2 == "5" :
            içecek = input("\n \n \nhangi içeceği içeceksiniz \n \n \n"
                           "\n \n \n1: küçük ayran - 10 tl  \n \n \n "
                           "\n \n \n2: büyük ayran - 15 tl \n \n \n "
                           "\n \n \n3: çay - 5 tl \n \n \n "
                           "\n \n \n4: ıce tea - 10 tl \n \n \n "
                           "\n \n \n5: su - 3tl \n \n \n")
            adet = int(input("\n \n \nkaç adet istersiniz :\n \n \n"))
            if içecek == "1":
                fiyat += 10 * adet 
            elif içecek == "2" : 
                fiyat += 15 * adet 
            elif içecek == "3":
                fiyat += 5 * adet 
            elif içecek == "4":
                fiyat += 10 * adet 
            elif içecek == "5" :
                fiyat += 3 * adet 
            else :
                print("\n \n \nhatalı sayı , düzgün sayı gir \n \n \n")

            sipariş_adedi += adet 
            print("\n \n \nsipariş alındı :",içecek,"\n \n \n")

        
        else:
            print("\n \n \nGeçersiz bir seçim yaptınız. Lütfen tekrar deneyin.\n \n \n")
    else:
        print("\n \n \nEvet ise 'E', hayır ise 'H' yi seçiniz.\n \n \n")