import main 

kg = int(input("bagaj ağırlığını girin : \n"))

ek_ücret = main.hesapla(kg)

if kg <= 20 : 
    print("ücrete gerek yok ")
elif kg > 20 :
    print("ücret : ",ek_ücret)