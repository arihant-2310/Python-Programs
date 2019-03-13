print("to print FIBONACCI series")
n= int(input("enter a number:-"))
f=0
s=1
print (f)
print(s)
for i in range(3,n+1):
    t= f+s
    print (t)
    f=s
    s=t

