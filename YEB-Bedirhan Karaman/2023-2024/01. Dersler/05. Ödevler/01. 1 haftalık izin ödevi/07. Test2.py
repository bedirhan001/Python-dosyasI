puan = 0
bonus_puan = 50

seçenek = input("genel kültür testi yapmak istermisiniz E-H : \n")
if seçenek == "h" or seçenek == "H" :
    print("tamam...")
elif seçenek == "e" or seçenek == "E" :
    print("başla o zaman")
    soru1 = input(" soru 1 : gül hangi şehirde meşhurdur ? : \n"
                "a) trakya \n"
                "b) ısparta \n"
                "c) tokat \n"
                "d) antalya \n")
    if soru1.lower() != "b":
        print("malesef yanlış, doğru cevap b idi ")
        print("puan:", puan)
    elif soru1.lower() == "b":
        puan += 10
        print("doğru cevap ")
        print("puan :", puan)

    soru2 = input("soru 2 : Hangi Ülkenin İki Tane Başkenti Vardır? \n"
                "a) güney afrika \n"
                "b) Senegal \n"
                "c) el-Salvador \n"
                "d) Kamboçya \n")

    if soru2.lower() != "a":
        print("malesef yanlış, doğru cevap a idi ")
        print("puan:", puan)
    elif soru2.lower() == "a":
        puan += 10
        print("doğru cevap ")
        print("puan :", puan)

    soru3 = input("soru3 : “Sinekli Bakkal” Romanının Yazarı Aşağıdakilerden Hangisidir? \n"
                "a) Reşat Nuri Güntekin \n"
                "b) Halide Edip Adıvar \n"
                "c) Ziya Gökalp \n"
                "d) ömer seyfettin \n")

    if soru3.lower() != "b":
        print("malesef yanlış, doğru cevap b idi ")
        print("puan:", puan)
    elif soru3.lower() == "b":
        puan += 10
        print("doğru cevap ")
        print("puan :", puan)

    soru4 = input("soru4 : Bir Sebepten Dolayı Tek Kulağına Küpe Takan Osmanlı Padişahı Kimdir?\n"
                "a) fatih sultan mehmet \n"
                "b) osman bey  \n"
                "c) abdülhamit han  \n"
                "d) yavuz sultan selim\n")
    if soru4.lower() != "d":
        print("malesef yanlış, doğru cevap d idi ")
        print("puan:", puan)
    elif soru4.lower() == "d":
        puan += 10
        print("doğru cevap ")
        print("puan :", puan)

    soru5 = input("Bonus soru: Dünya üzerindeki en büyük okyanus hangisidir?\n"
                  "a) pasifik okayanusu\n"
                  "b) hint okyanusu \n"
                  "c) atlas okyanusu\n"
                  "d) güney okyanusu\n")
    if soru5.lower() == "a":
        puan += bonus_puan
        print("Doğru cevap! Bonus puan kazandınız.")
        print("Toplam puan:", puan)
    elif soru5.lower() != "a" :
        print("Malesef yanlış, doğru cevap a idi.")
        print("Toplam puan:", puan)

    soru6 = input("soru6 : Dünya tarihindeki ilk yazılı hukuk kurallarının bulunduğu antik Mezopotamya bölgesindeki şehir devleti nedir? \n"
                "a) Roma\n"
                "b) Atil\n"
                "c) Babil\n"
                "d) Mısır\n")
    if soru6.lower() != "c":
        print("malesef yanlış, doğru cevap c idi" )
        print("puan:", puan)
    elif soru6.lower() == "c":
        puan += 10
        print("doğru cevap ")
        print("puan :", puan)

    soru7 = input("soru7 : Nobel Fizik Ödülü'nü alan ilk kadın kimdir? \n"
                "a) Dorothy Crowfoot Hodgkin\n"
                "b) Rosalind Franklin\n"
                "c) Gerty Cori\n"
                "d) Marie Curie\n")
    if soru7.lower() != "d":
        print("malesef yanlış, doğru cevap d idi" )
        print("puan:", puan)
    elif soru7.lower() == "d":
        puan += 10
        print("doğru cevap ")
        print("puan :", puan)

    if puan <= 50:
        print("Yani biraz geliştirmen gerek \n")
    elif 110 > puan > 50:
        print("Güzel ama daha iyi olabilir ")
    elif puan == 110 :
        print("çok iyi böyle devam et dostum ")