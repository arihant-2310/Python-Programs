n= input('enter the number of elemente:-')
print'Enter elements'
l=[]
for i in range(n):
    e= input()
    l.insert(i,e)
print'the list id:-'
print l
p= input('enter element position which is to be replaced:-')
b= l[p-1]
l.remove(b)
ele= input('enter the element to be addes:-')
l.insert(p-1,ele)
print'the new list is:-'
print l
