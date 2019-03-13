print("to print armstrong number within a limit using function")
def armstrong(n):
    t=n
    s=0
    k=0
    while n>0:
        k=k+1
        n=n//10
    n=t
    while n>0:
        r= n%10
        s= s+r**k
        n=n//10
    if s==t:
        return True
    else:
        return False
l= int(input("enter lower limit:-"))
u= int(input("enter upper limit:-"))
print("the armstrong nos. are")
for i in range(l+1,u):
    if(armstrong(i)):
        print (i)
    
