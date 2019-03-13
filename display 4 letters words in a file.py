fname= raw_input('enter file name to open-')
f1= open(fname,'r')
text= f1.read()
l= text.split(" ")
cnt=0
for i in l:
    if len(i)==4:
        print i,
        cnt=cnt+1
print 'no. of 4 letters word-',cnt
