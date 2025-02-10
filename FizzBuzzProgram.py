## FizzBuzzProgram

def getCase(num):
    result = 0
    if num%3==0 :  
        result += 1
    if num%5==0:
        result += 2
    return result

for i in range(1, 101):
    myCase = getCase(i)
    
    match myCase:
        case 0:
            print(i)
        case 1: 
            print("Fizz")
        case 2: 
            print("Buzz")
        case 3:
            print("FizzBuzz")