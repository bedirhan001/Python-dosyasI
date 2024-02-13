ilk = int(input("başlangıç için sayıyı giriniz: \n"))
son = int(input("son sayıyı girin:\n "))

toplam = 0 

while ilk < son :
    ilk += 1
    toplam += ilk 

print("toplamı :",toplam)