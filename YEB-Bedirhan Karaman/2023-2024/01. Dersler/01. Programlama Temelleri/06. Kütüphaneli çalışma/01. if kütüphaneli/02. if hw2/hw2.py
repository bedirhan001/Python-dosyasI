import main 

angle1 = int(input("1. açıyı girin : \n"))
angle2 = int(input("2. açıyı girin : \n"))
angle3 = int(input("3. açıyı girin : \n"))

ort = main.angle(angle1,angle2,angle3)

if ort == 180 : 
    print("bu bir üçgendir ")
else : 
    print("bu bir üçgen değilldir ...")