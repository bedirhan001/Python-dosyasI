a = input("sinemamı, tiyatromu: ")
b = input("öğrenci misiniz, sivil misiniz: ")

if a == "sinema" and b == "sivil":
    print("15 TL")
elif a == "sinema" and b == "öğrenci":
    print("7.5 TL")
elif a == "tiyatro" and b == "sivil":
    print("10 TL")
elif a == "tiyatro" and b == "öğrenci":
    print("5 TL")