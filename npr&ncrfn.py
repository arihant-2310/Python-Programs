print("to find ncr and npr")
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
n= int(input("enter a number n:-"))
r= int(input("enter value of r:-"))
print("permutation=",fact(n)/fact(n-r))
print("combination =",fact(n)/fact(n-r)*fact(r))
