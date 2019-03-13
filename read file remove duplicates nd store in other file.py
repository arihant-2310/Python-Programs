import pickle
def display(f):
    try:
        while True:
            num= pickle.load(f)
            print num
    except EOFError:
        pass
#reading numbers
fname1= raw_input('enter file name to read the numbers-')
f1= open(fname1,'w+')
n= input('enter how many numbers-')
print'enter the numbers-'
i=1
while i<=n:
    num= input('enter-')
    pickle.dump(num,f1)
    i=i+1
f1.seek(0)
print fname1,'contents:\n'
display(f1)
#reading file and storing in list after removing duplicates
f1.seek(0) 
l=[]
try:
    while True:
        num= pickle.load(f1)
        if num not in l:
            l.append(num)
        i=i+1
except EOFError:
    pass
y= sorted(l)
fname2= raw_input('enter file name to store the sorted nos. after removing duplicates-')
f2= open(fname2,'w+')
i=1
for i in y:
    pickle.dump(i,f2)
f2.seek(0)
print fname2,'contents:\n'
display(f2)
    
        
