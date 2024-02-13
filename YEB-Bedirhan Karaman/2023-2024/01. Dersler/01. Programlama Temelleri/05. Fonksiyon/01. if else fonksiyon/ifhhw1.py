def get_note():
    note1 = int(input("not gir :"))
    note2 = int(input("not gir :"))
    note3 = int(input("not gir :"))
    return note1 + note2 + note3 

total = get_note()

ort = total / 3 

if ort <= 50 :
    print("başarısız")
elif ort > 50 :
    print("başarılı")