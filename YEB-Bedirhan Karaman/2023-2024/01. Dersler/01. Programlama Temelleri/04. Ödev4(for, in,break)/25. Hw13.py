tek_sayilar = []
for sayi in range(1, 31):
    if sayi % 2 == 0:
        continue
    tek_sayilar.append(sayi)

print("1-30 arasındaki tek sayılar:")
print(tek_sayilar)