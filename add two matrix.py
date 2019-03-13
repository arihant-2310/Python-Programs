m= input('enter the no. of rows of first matrix-')
n= input('enter the no. of columns of first matrix-')
p= input('enter the no. of rows of second matrix-')
q= input('enter the no. of columns of second matrix-')
print('enter the first matrix elements-')
mat1=[]
mat2=[]
for i in range(m):
    mat1.append([])
    for j in range(n):
        e= input('enter element of 1st matrix-')
        mat1[i].append(e)
print'first matrix is-'
for i in range(m):
    for j in range(n):
        print mat1[i][j],
    print
for i in range(p):
    mat2.append([])
    for j in range(q):
        e= input('enter element of second matrix-')
        mat2[i].append(e)
print'second matrix is-'
for i in range(p):
    for j in range(q):
        print mat2[i][j],
    print
mat3=[]
if m==p and n==q:
    for i in range(m):
        mat3.append([])
        print
        for j in range(n):
             mat3[i].append(mat1[i][j]+mat2[i][j]),
    print 'sum of the matrices are-'
    for i in range(m):
        for j in range(n):
            print mat3[i][j],
        print
else:
    print'addition not possible'
