st= raw_input('enter a string which contains punctuation mark-')
fname= raw_input('enter file name to open-')
f= open(fname,'w+')
f.write(st)
f.seek(0)
c= f.read(1)
str1=""
p= ['.',',',':',';','!','(',')','{','}','[',']','/','\',','?','-','_']
while c!="":
    if c not in p:
        str1= str1+c
    c= f.read(1)
print'the string is-',str1
f.close()
