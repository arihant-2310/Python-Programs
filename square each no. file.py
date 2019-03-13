import pickle
fname= raw_input('enter file name to open-')
f= open(fname,'w+')
print'enter 10 numbers-'
i=1
while i<=10:
     num= input('enter number-')
     pickle.dump(num,f)
     i=i+1
f.seek(0)
try:
    while True:
        num= pickle.load(f)
        print num,':',num*num
except EOFError:
    pass
