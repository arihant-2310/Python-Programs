print("to check if a number is armstrong")
n= int(input("enter a number:-"))
k=0
m=n
t=n
a=0
while n>0:
    k=k+1
    n=n//10
while(m>0):
    r= m%10
    a= a+ r**k
    m=m//10
if t==a:
    print("it is an armstrong number")
else:
    print("it is not an armstrong number")

