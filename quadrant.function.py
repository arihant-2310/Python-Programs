print("to find the quadrant of given x-y coordinates")
def quadrant(x,y):
    if x>=0 and y>=0:
        print("the coordinates lies in first quadrant")
    elif x<0 and y>0:
        print("the coordinates lies in second quadrant")
    elif x<0 and y<0:
        print("the coordinates lies in third quadrant")
    elif x>0 and y<0:
        print("the coordinate lies in forth quadrant")
x= int(input('enter x coordinate:-'))
y= int(input('enter y coordinate:-'))
quadrant(x,y)
