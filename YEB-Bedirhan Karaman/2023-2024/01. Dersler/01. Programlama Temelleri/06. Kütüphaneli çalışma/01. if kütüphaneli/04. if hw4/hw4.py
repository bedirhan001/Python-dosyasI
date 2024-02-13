import main

numbers = main.numbers()

if numbers > 200 : 
    indirim = numbers - (numbers*0.25)
    print(indirim)
elif numbers < 200 : 
    print(numbers)