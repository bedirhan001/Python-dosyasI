hour = int(input("kaç saat kaldığınızı giriniz :"))

ek = hour*4
ek2 = hour*3

if hour <= 1 :
    print("ücret : 5tl")
elif 1 < hour < 5 : 
    print("ödenecek ücret :",ek)
else : 
    print("ödenecek ücre :",ek2)

    