import pickle
fname1= raw_input('enter file name to open-')
fname2= raw_input('enter file name to store odd nos-')
fname3= raw_input('enter file name to store even nos-')
f1= open(fname1,'w+')
n= input('enter the number of elements-')
i=1
print'enter elements-'
while i<=n:
    num=input()
    pickle.dump(num,f1)
    i=i+1
f1.seek(0)
try:
    f2= open(fname2,'w+')
    f3= open(fname3,'w+')
    while True:
        y= pickle.load(f1)
        if y%2==0:
            pickle.dump(y,f3)
        else:
            pickle.dump(y,f2)
except EOFError:
    pass
