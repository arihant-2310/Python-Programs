class person:
    name=" "
    age=0
    salary=0
    def display(self):
        print self.name,self.age,self.salary
p1= person()
p2=person()
p1.name= raw_input('enter name-')
p1.age= input('enter age-')
p1.salary= input('enter salary-')
print
p2.name= raw_input('enter name-')
p2.age= input('enter age-')
p2.salary= input('enter salary-')
print
p1.display()
p2.display()
