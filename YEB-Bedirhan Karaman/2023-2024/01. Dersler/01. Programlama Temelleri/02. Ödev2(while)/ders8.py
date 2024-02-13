ilk = 20
son = 50

toplam = 0

while ilk <= son:
    if ilk % 2 == 0:
        toplam += ilk
    ilk += 1

print("20 ile 50 arasındaki çift sayıların toplamı:", toplam)