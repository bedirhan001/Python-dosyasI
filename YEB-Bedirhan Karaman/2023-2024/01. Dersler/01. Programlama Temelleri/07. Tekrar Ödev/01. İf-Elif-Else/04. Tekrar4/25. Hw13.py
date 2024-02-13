name  = input("adınızı giriniz :")
year = float(input("çalışma yılını giriniz :"))
maaş = int(input("maaşınızı giriniz :"))

if 0 < year < 5 :
    zam = 0.10
elif 6 < year < 10 : 
    zam = 0.15 
elif year > 15 :
    zam = 0.25

zam_miktari = maaş * zam

zamli_maas = maaş + zam_miktari

print("sayın ",name,"maaşınız zamdan sonra",zamli_maas)