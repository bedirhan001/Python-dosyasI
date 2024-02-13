 #ilk ürünü iste 

def get_product():
    product_1 = int(input("ürünün fiyatını girin : "))
    product_2 = int(input("ürünün fiyatını girin : "))
    return product_1 + product_2

 #sonra al 

total = get_product()

 #indirimi tanımla 
discount = total - (0.25 * total ) 

if total >= 200 :
    print(discount)
elif total < 200 :
    print(f"ücret {total}")