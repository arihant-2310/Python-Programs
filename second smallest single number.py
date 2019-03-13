a=[]
n= input('enter number of elements:-')
for i in range(n):
    e= input('enter element')
    a.append(e)
a.sort()
print('second smallest element:-')
print a[1]
