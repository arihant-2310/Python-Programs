fname= raw_input('enter file name-')
f1= open(fname,'r+')
c= f1.read()
c= c.replace(" ",'_')
f1.seek(0)
f1.write(c)
f1.seek(0)
print f1.read()
f1.close()
