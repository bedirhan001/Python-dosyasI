def couple_number():
    for numbers in range(0,20):
        return numbers 
    
def question(numbers):
    if numbers % 2 == 0 :
        return question                             # HATALI
    
numbers = couple_number()

print(question(numbers))