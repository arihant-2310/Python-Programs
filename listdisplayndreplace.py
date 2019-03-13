print(" to create a list,display it & replace a element with given position to other element")
n= int(input("enter how many elements:-"))
print("enter the elements-")
l=[]
for i in range(n):
    e= input()
    l.insert(i,e)
print("the list is:-")
for i in l:
    print(i,)
pos= input("enter the position of element which u want to replace:-")
ele= int(input("new element"))
for i in l:
    if i==pos:
         l.remove(i)
l.insert(i,ele)
    
print("the new list after replacing")
for i in l:
    print (i)

       
