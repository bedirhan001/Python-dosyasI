hour = float(input("Otoparkta kaç saat kaldınız: "))

if hour <= 1:
    print ("ücret 5tl") 
elif hour <= 5:
    print ( "ücret :",5 + (hour - 1) * 4 ) 
else:
    fiyat = 5 + 4 * 4 + (hour - 5) * 3

print("ücret :", fiyat)