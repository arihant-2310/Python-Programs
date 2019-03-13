print'\t\ttelephone number and names'
n= input('enter how many persons=')
i=1
d={}
while i <=n:
    name= raw_input('enter name-')
    tno= input('enter your phone numbers-')
    d[name]= tno
    i=i+1
for i in sorted(d.keys()):
    print i,':',d[i]
