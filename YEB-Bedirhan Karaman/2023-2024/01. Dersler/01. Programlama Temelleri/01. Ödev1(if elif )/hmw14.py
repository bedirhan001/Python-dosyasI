n1 = float(input("1. sayıyı giriniz :"))
n2 = float(input("2. sayıyı giriniz :"))
n3 = float(input("3. sayıyı giriniz :"))

if n1 > n2  and n1 > n3:
    print("en büyük sayı :",n1)
elif n2 > n1 and n2 > n3 :
    print("en büyük sayı :",n2)
elif n3 > n1 and n3 > n2 :
    print("en büyük sayı :",n3)