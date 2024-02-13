ders = ['B', 'İ', 'L', 'İ', 'Ş', 'İ', 'M']
ders.sort()
print(ders)

ters_ders = ders[::-1]
print(ters_ders)

sayi_i = ders.count('İ')
print("İ harfi sayısı:", sayi_i)

istenen_harfler = ['B', 'İ', 'L', 'İ', 'M']
filtrelenmis_ders = [harf for harf in ders if harf in istenen_harfler]
print(filtrelenmis_ders)

alan = ders.copy()
print(alan)

ders.clear()
print(ders)

index_l = alan.index('L')
print("L'nin indeksi:", index_l)
