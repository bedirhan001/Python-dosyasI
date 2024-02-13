s1 = input("tiyatro yada sinema seçiniz ")
s2 = input("öğrenci yada sivil olduğunuzu yazınız ")

if s1 == "sinema :" :
    if s2 == "sivil ":
        print("15tl")
    else :
        print("7.5tl")
elif s1 == "tiyatro ": 
    if s2 == "sivil":
        print("10tl")
    else :
        print("5tl")