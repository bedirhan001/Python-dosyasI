boy = float(input("boyunuzu girin :"))
kg = int(input("ağırlığınızı girin :"))

VKİ=kg/(boy*boy)

print("vki :",VKİ)
if  18 < VKİ < 25 :
    print("normal")
elif 25 < VKİ < 30 :
    print("kilolu")
elif 30 < VKİ < 34 :
    print("obez")
elif VKİ > 35 :
    print("yüksek obez")