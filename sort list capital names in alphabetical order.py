l=[]
n= input('how many numbers-')
for i in range(n):
    e= raw_input('enter name-')
    l.append(e)
l.sort()
for j in range(n):
    l[i]= l[i].upper()
print'the sorted capital list is:-'
print l
print
