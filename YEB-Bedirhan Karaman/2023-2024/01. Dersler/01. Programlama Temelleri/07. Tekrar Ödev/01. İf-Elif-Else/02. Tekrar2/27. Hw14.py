n1 = int(input("birinci sayıyı giriniz :"))
n2 = int(input("ikinci sayıyı giriniz :"))
n3 = int(input("üçüncü sayıyı giriniz :"))

if n1 > n2 and n1 > n3 :
    print("en büyük sayı ,1. sayı :",n1)
elif n2 > n1 and n2 > n3 :
    print("en büyük sayı ,2. sayı :",n2)
elif n3 > n1 and n3 > n2 :
    print("en büyük sayı ,3. sayı :",n3)
elif n1 == n2 :
    print("en büyük sayılar 1 ve 2 :",n1 ,n2 )
elif n1 == n3 :
    print("en büyük sayılar 1 ve 3 :",n1 ,n3 )
elif n2 == n3 :
    print("en büyük sayılar 2 ve 3 :",n2 ,n3 )