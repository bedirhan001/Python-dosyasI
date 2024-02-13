n1 = int(input("1. sayıyı gir: "))
n2 = int(input("2. sayıyı gir: "))
toplam = 0

for a in range(n1, n2 + 1):
    toplam += a

print("toplamı : ",toplam)