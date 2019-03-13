fname= raw_input('enter file name to open-')
f1= open(fname,'r')
str= f1.readline()
l = str.split(" ")
for i in l:
    if i==i[::-1]:
        print i

