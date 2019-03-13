fname= raw_input('enter file name to open-')
f= open(fname,'r')
c= f.read()
l= c.split(" ")
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
for i in l1:
    cnt= c.count(i)
    print i,':',cnt
f.close()
