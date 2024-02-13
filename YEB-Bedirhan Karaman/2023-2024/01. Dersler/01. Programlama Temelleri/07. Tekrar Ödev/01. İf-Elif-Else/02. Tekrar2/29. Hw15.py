seçim = input("sinema yada tiyatro :")
seçim2 = input("sivil yada öğrenci olduğunuzu seçiniz :")


if seçim == "sinema" :
    if seçim2 == "sivil" :
        print("ücret : 15")
    elif seçim2 == "öğrenci" :
        print("ücret : 7.5")
elif seçim == "tiyatro" : 
    if seçim2 == "sivil" :
        print("ücret : 10")
    elif seçim2 == "öğrenci" :
        print("ücret : 5")