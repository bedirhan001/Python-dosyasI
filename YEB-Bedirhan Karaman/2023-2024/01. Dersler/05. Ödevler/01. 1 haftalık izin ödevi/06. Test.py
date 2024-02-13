#  testi 
doğru_cevap = 0 
yanlış_cevap = 0 

soru1 = input("soru 1 : \n"
              "matematikte 0 (sıfırı) kim bulmuştur \n"
              "a) pisagor \n"
              "b) aristo \n"
              "c) arşimet \n"
              "d) harezmi \n")

if soru1 != "d" :
    yanlış_cevap += 1 
elif soru1 == "d" :
    doğru_cevap += 1 
else : 
    print("seçtiğiniz cevap yanlış olarak değerlenecek")

soru2 = input("soru 2 \n"
              "aşağıdakilerden hangisinin cevabı 1 dir \n"
              "a) 0 ∧ 1 \n"
              "b) 1 => 0 \n"
              "c) 1 v 1 \n"
              "d) 1 ⇔ 0 \n")

if soru2 != "c" :
    yanlış_cevap += 1 
elif soru2 == "c" :
    doğru_cevap += 1 
else : 
    print("seçtiğiniz cevap yanlış olarak değerlenecek")

soru3 = input("soru 3 \n"
              "3+5(4/2)-10 işleminin cevabı nedir \n"
              "a) 16 \n"
              "b) 0 \n"
              "c) 6 \n"
              "d) 10 \n")

if soru3 != "c" :
    yanlış_cevap += 1 
elif soru3 == "c" :
    doğru_cevap += 1 
else : 
    print("seçtiğiniz cevap yanlış olarak değerlenecek")

soru4 = input("soru 4 \n "
              "Türk hanlarının yaşadığı çerge olarak da bilinen büyük ve süslü çadırın adı nedir? \n"
              "a) otağ \n"
              "b) kümbet \n"
              "c) oba \n"
              "d) hiçbiri \n")

if soru4 != "a" :
    yanlış_cevap += 1 
elif soru4 == "a" :
    doğru_cevap += 1 
else : 
    print("seçtiğiniz cevap yanlış olarak değerlenecek")

soru5 = input("soru 5 \n "
              "Türkiye’ de kaç tane coğrafi bölge bulunmaktadır? \n"
              "a) 3 \n"
              "b) 4 \n"
              "c) 5 \n"
              "d) 7 \n")

if soru5 != "d" :
    yanlış_cevap += 1 
elif soru5 == "d" :
    doğru_cevap += 1 
else : 
    print("seçtiğiniz cevap yanlış olarak değerlenecek")

soru6 = input("soru 6 \n "
              "Gülü ile meşhur olan ilimiz hangisidir? \n"
              "a) tokat \n"
              "b) ısparta \n"
              "c) tekirdağ \n"
              "d) eskişehir \n")

if soru6 != "b" :
    yanlış_cevap += 1 
elif soru6 == "b" :
    doğru_cevap += 1 
else : 
    print("seçtiğiniz cevap yanlış olarak değerlenecek")

soru7 = input("soru 7 \n "
              "1071’de yapılan Malazgirt Savaşıyla Anadolu’nun kapılarını Türklere açan Selçuklu Sultanı kimdir? \n"
              "a) fatih sulan mehmet \n"
              "b) Sultan Alparslan \n"
              "c) osman bey \n"
              "d) Sultan Alaaddin \n")

if soru7 != "b" :
    yanlış_cevap += 1 
elif soru7 == "b" :
    doğru_cevap += 1 
else : 
    print("seçtiğiniz cevap yanlış olarak değerlenecek")

soru8 = input("soru 8 \n "
              "Gezilerini ‘Seyahatname’ adlı eserde toplayan Türk gezgin kimdir? \n"
              "a) harezmi \n"
              "b) piri reis \n"
              "c) Katip Çelebi \n"
              "d) Evliya Çelebi \n")

if soru8 != "d" :
    yanlış_cevap += 1 
elif soru8 == "d" :
    doğru_cevap += 1 
else : 
    print("seçtiğiniz cevap yanlış olarak değerlenecek")

soru9 = input("soru 9 \n "
              "Osmanlı Devletinin kurucusu olan Osmanlı ailesi hangi Türk boyuna mensuptur? \n"
              "a) Kayı \n"
              "b) Bozok  \n"
              "c) karahanlı \n"
              "d) hepsi \n")

if soru9 != "a" :
    yanlış_cevap += 1 
elif soru9 == "a" :
    doğru_cevap += 1 
else : 
    print("seçtiğiniz cevap yanlış olarak değerlenecek")

soru10 = input("soru 10 \n "
              "Bozkırın tezenesi lakaplı rahmetli halk ozanı kimdir? \n"
              "a) Neşet Ertaş \n"
              "b) Kıvırcık Ali  \n"
              "c) sait faik  \n"
              "d) hiçbiri \n")

if soru10 != "a" :
    yanlış_cevap += 1 
elif soru10 == "a" :
    doğru_cevap += 1 
else : 
    print("seçtiğiniz cevap yanlış olarak değerlenecek")
    yanlış_cevap += 1 
print("toplamda",doğru_cevap,"tane doğru ,",yanlış_cevap,"tane yanlış var ")
if doğru_cevap < 5 : 
    print("geliştirilmeli")
elif doğru_cevap >= 5 : 
    print("güzel .. ")