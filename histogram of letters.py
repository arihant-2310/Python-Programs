st= raw_input('enter string:-')
d={}
for i in st:
    if i not in d:
        d[i]=1
    else:
        d[i]= d[i]+1
print'histogram of letters in ',st
for i in sorted(d.keys()):
    print i,':',d[i]
