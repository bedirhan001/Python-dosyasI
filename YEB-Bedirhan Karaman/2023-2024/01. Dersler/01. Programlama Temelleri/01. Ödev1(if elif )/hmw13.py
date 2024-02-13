ad = input("Adınızı giriniz: ")
maas = float(input("Maaşınızı giriniz: "))
calisma_yili = int(input("Çalışma yılınızı giriniz: "))

if 0 <= calisma_yili <= 5:
    zam_orani = 0.10
elif 6 <= calisma_yili <= 10:
    zam_orani = 0.15
else:
    zam_orani = 0.25

zam_miktari = maas * zam_orani

zamli_maas = maas + zam_miktari

print("Sayın:", ad, "zamlı maaşınız:", zamli_maas, "TL")