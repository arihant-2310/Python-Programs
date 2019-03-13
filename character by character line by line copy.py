fname1= raw_input('enter filename to open-')
fname2= raw_input('enter file name to store character by character-')
fname3= raw_input('enter file name to store line by line-')
try:
    f1= open(fname1,'r')
    f2= open(fname2,'w+')
    f3= open(fname3,'w+')
    c= f1.read(1)
    while c!="":
        f2.write(c)
        f2.read(1)
    f2.seek(0)
    print f2.read()
    f2.close()
    f1.seek(0)
    d= f1.readline()
    while D!="":
        f3.write(d)
        f1.readline()
    f3.seek(0)
    print f3.read()
    f3.close()
    f1.close()
except EOFError:
    print'file doesnot exist'
