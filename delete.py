n= input('enter how many elements in the list-')
l=[]
for i in range(n):
    e= input('enter element-')
    l.append(e)
print'the list is-',l
de= input('enter the element to be deleted-')
for i in l:
    if i==de:
        l.remove(de)
        print'element deleted'
        break
else:
    print'element not found'
print'the list after deletion is-',l
