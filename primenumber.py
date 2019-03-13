print("to check if a number is PRIME")
n= int(input("enter a number:-"))
i=1
prime=1
for i in range(2,n//2+1):
    if n%i==0:
        print("it is not a prime number")
        prime=0
        break
    else:
        i=i+1
if prime==1:
    print("it is a prime number")

    
