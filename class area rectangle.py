class rectangle:
    length=0.0
    breadth= 0.0
    def area(self):
        print'\tAREA-',self.length*self.breadth
r1= rectangle()
r2= rectangle()
print'\tENTER LENGTH AND BREADTH OF FIRST RECTANGLE-'
r1.length= input('length-')
r1.breadth= input('breadth-')
print'\tENTER LENGTH AND BREADTH OF SECOND RECTANGLE-'
r2.length= input('length-')
r2.breadth= input('breadth-')
print'\t area of first rectangle'
r1.area()
print'\tarea of second rectangle'
r2.area()
