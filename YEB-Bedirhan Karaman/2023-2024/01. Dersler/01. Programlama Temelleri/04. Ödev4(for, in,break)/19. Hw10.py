kelimeler = input("istediğini gir :")
toplam = 0

for kelime in kelimeler :
    if kelime == "a" or kelime == "A":
        toplam += 1
print("girdiğiniz değerde ",toplam," tane 'a' bulunuyo ")