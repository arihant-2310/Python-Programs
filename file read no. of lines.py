fname= input("enter file name to open:-")
f1= open(fname,'r')
num_lines=0
for line in f1:
    num_lines= num_lines+1
print("number of lines=",num_lines)
