st= raw_input('enter the string-')
capstr=""
for i in range(len(st)):
    if st[i].islower():
        capstr=capstr+st[i].upper()
    else:
        capstr= capstr+st[i]
print capstr
