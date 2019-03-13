print("to find the factorial of a given number using recursive function")
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
n= int(input("enter a number:-"))
print("the factorial of given number is:-",fact(n))
