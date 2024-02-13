def gettext():
    return input("metni gir ")

def hesapla(letter):
    row = ""
    for i in range(1,11):
        row += letter 
    return row 

user_input = gettext()


result_row = hesapla(user_input)


print(result_row)
