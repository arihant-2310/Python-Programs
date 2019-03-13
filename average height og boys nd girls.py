n= input('enter number of students:-')
student= []
print'\t\tENTER STUDENT DETAILS'
i=1
while i<=n:
    name= raw_input('enter name-')
    rno= input('enter roll number-')
    gender= raw_input('enter your gender(M/F)-')
    height= input('enter height in cms-')
    student.append((name,rno,gender,height))
    print
    i= i+1
print'\t\tDETAILS OF STUDENTS'
print student
print
print
(nb,ng,hb,hg)=(0,0,0,0)
for i in student:
    if i[2]=='f'or i[2]=='F':
        ng= ng+1
        hg= hg+i[3]
    elif i[2]=='m'or i[2]=='M':
        nb= nb+1
        hb= hb+i[3]
    else:
        print'invalid entry'
print'average height of girls-',hg/ng
print'average height of boys-',hb/nb
        
