print("to display the count of 4 letter word in a file")
fname= input("enter file name:-")
f= open(fname,'r')
d=0
c= f.read()
print(c)
l= c.split()
for word in l:
    if len(word)==4:
        d=d+1
print("number of 4 letter words are:-",d)
