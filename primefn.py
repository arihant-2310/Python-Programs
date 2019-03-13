print("to find a number is prime or not using function")
def prime(n):
    i=2
    p=1
    while i<=n/2:
        if n%i==0:
            print("it is not a prime number")
            p= 0
            break
        else:
            i=i+1
    if p==1:
        print("it is a prime number")
        
n= int(input("enter the number-"))
prime(n)
