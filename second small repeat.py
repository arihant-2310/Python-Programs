l=[]
n= input('enter number of elements:-')
for i in range(n):
    e= input('enter element:-')
    l.append(e)
new= sorted(l)
print new
print
min= new[0]
for j in range(n):
    if min in new:
        new.remove(min)
    else:
        break
for x in range(n):
    if l[x]==new[0]:
        print'second smallest',new[0]
        print'position-',x+1
