def kullanıcı_adı():
    return input("adını gir : ")

def maaş():
    return float(input("maaşını gir : "))

def yıl():
    return int(input("yılı gir : "))


ad = kullanıcı_adı()
para = maaş()
çalışma_yılı = yıl()



if 0 < çalışma_yılı <= 5 :
    zam = 0.5 
elif 6 <= çalışma_yılı <=  10 : 
    zam = 0.10 
elif çalışma_yılı > 11 : 
    zam = 0.25 

zamlı_maaş = (para * zam ) + para 

print("sayın ",ad,"maaşınız zamdan sonra ",zamlı_maaş)