n= input('enter how many numbers:-')
l= []
for i in range(n):
    e= input('enter elements-')
    l.append(e)
for i in range(n):
    for j in range(n-1-i):
        if l[j]>l[j+1]:
            t= l[j]
            l[j]= l[j+1]
            l[j+1]= t
print'sorted list is:-'
print l
