print("to simulate a menu driven program which perform addition,subtraction,multiplication and exponentiation using function")
def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b
def exp(a,b):
    return a**b
#main program
a= int(input("enter first number"))
b= int(input("enter second number"))
while(True):
    print("SIMPLE CALCULATOR")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exponentation")
    print("press any number to exit!!")
    print()
    choice=int(input("enter your choice(1-5):-"))
    if choice==1:
        print(addition(a,b))    
    elif choice==2:
        print(subtraction(a,b))
    elif choice==3:
        print(multiplication(a,b))
    elif choice==4:
        print(division(a,b))
    elif choice==5:
        print(exp(a,b))
    else:
        break
        
