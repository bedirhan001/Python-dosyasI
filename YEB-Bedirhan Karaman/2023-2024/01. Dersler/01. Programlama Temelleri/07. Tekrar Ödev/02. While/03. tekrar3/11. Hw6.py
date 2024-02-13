start = int(input("başlangıç sayısını seçiniz :"))
stop = int(input("son sayıyı giriniz :"))
toplam = 0

while start <= stop :
    toplam += start 
    start += 1
print("arasındaki sayıların toplamı :",toplam)