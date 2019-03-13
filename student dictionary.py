print'\t\t STUDENT DETAILS'
student={}
i=1
print'enter the details of 5 students'
while i<=5:
    print
    print'enter details of',i,'student'
    rno= input('enter roll number-')
    name= raw_input('enter name -')
    mark1= input('enter mark1-')
    mark2= input('enter mark2-')
    mark3= input('enter mark3-')
    student[rno]= (name,mark1,mark2,mark3)
    i=i+1
print student
(mx,rno)=(0,0)
for i in sorted(student.keys()):
    total= student[i][1]+student[i][2]+student[i][3]
    student[i]= student[i]+(total,)
    if total>mx:
        (mx,rno)=(total,i)
print'student with highest mark-',student[rno]
    
