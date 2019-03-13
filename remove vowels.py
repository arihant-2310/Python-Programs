st= raw_input('enter string-')
l= ['a','e','i','o','u','A','E','I','O','U']
newstr=""
for i in range(len(st)):
    if st[i] not in l:
        newstr= newstr+st[i]
print newstr
