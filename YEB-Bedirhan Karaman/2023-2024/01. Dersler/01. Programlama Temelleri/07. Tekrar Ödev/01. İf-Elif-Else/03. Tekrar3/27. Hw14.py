s1 = int(input("birinci sayıyı giriniz :"))
s2 = int(input("ikinci sayıyı giriniz :"))
s3 = int(input("üçüncü sayıyı giriniz :"))

if s1 > s2 and s1 > s3 :
    print("en büyük sayı, sayı bir :",s1)
elif s2 > s3 and s2 > s1 :
    print("en büyük sayı ,sayı 2 :",s2)
else :
    print("en büyük sayı,sayı 3 :",s3)