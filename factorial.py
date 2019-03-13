print("To find the factorial of a given number")
n= int(input("enter a number to find the factorial of-"))
fact=1
for i in range(1,n+1):
    fact= fact *i
    i=i+1
print("the factorial is:-",fact)
