islemci = input("İşlemci türünü girin : ")
ram = int(input("RAM bellek miktarını girin :"))

if islemci == "i7" and ram <= "8" :
    print("kurulum uygun")
else :
    print("kurulum uygun değil")