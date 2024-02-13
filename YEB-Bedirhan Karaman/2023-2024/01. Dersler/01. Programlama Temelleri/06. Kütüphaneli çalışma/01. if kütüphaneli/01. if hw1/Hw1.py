import main 

note1 = int(input("1. notu girin : \n"))
print("--"*10)
note2 = int(input("2. notu girin : \n"))
print("--"*10)
note3 = int(input("3. notu gir : \n"))
print("--"*10)

total = main.get_note(note1,note2,note3)

if total >= 50 : 
    print("başarılı ")
elif total < 50 : 
    print("başarısız ")