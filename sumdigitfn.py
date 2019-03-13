print("to find the sum of digits")
def sum_digit(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        r= n%10
        return r+ sum_digit(n//10)
n= int(input("enter a number:-"))
print("sum of the digits",sum_digit(n))
