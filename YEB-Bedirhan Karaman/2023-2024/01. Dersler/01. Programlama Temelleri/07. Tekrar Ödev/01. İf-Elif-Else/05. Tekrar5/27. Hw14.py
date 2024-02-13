a1 = int(input("birinci sayıyı giriniz :"))
a2 = int(input("ikinci sayıyı giriniz :"))
a3 = int(input("üçüncü sayıyı giriniz :"))

if a1 > a2 and a1 > a3 :
    print("en büyük sayı ilk sayı :",a1)
elif a2 > a1 and a2 > a3 :
    print("en büyük sayı ikinci sayı :",a2)
elif a3 > a1 and a3 > a2 :
    print("en büyük sayı üçüncü sayı :",a3)
elif a1 == a2 :
    print("en büyük sayı birinci ve ikinci sayı :",a1,a2)
elif a1 == a3 :
    print("en büyük sayı birinci ile üçüncü sayı :",a1,a3)
elif a2 == a3 :
    print("en büyük sayı ikinci ve üçüncü sayı:",a2 ,a3)
else :
    print("en büyük sayı birinci , ikinci ve üçüncü sayı :",a1,a2,a3)