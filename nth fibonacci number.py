fib={1:0,2:1}
n= input('nth fibonacii number-')
for i in range(3,n+1):
    fib[i]= fib[i-2]+fib[i-1]
print n,'th fibonacci number is-',fib[n]
