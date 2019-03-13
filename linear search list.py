n= input('enter the number of elements:-')
print'enter the elements:-'
l=[]
for i in range(n):
    e= input()
    l.insert(i,e)
print'the list is:-'
print l
print
ele= input('enter the element to be searched:-')
for i in range(n):
    if l[i]==ele:
        print 'element found'
        print'position-',i+1
        break
else:
    print'element not found'
    
