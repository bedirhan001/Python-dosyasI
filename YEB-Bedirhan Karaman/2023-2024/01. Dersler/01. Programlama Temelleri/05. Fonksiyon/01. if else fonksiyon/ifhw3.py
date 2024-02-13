def getbaggage():
    baggage = float(input("Bagaj ağırlığını gir : \n"))
    return int(baggage)

def hesaplayıcı(baggage):
    if baggage <= 20 : 
        return 0 
    return baggage - 20 

def hesaplayıcı_2(hesap):
    if hesap <= 0:
        return 0  
    else:
        fee_rate = 10
        additional_fee = hesap * fee_rate
        return additional_fee


baggage_weight = getbaggage()
excess_weight = hesaplayıcı(baggage_weight)
additional_fee = hesaplayıcı_2(excess_weight)

print("Additional Fee:", additional_fee)
