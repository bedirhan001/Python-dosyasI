def angles():
    angle_1 = int(input("açıyı gir : "))
    angle_2 = int(input("açıyı gir : "))
    angle_3 = int(input("açıyı gir : "))
    return angle_1 + angle_2 + angle_3 



total = angles()


if total == 180 : 
    print("bu bir üçgendir ")
elif total != 180 : 
    print("bu bir üçgen değill")