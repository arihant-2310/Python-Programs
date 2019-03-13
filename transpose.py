m= input('enter number of rows-')
n= input('enter number of columns-')
print'enter matrix elements-'
mat=[]
for i in range(m):
    mat.append([])
    for j in range(n):
        e= input('enter element-')
        mat[i].append(e)
for i in range(m):
    for j in range(n):
        print mat[i][j],
    print
trans=[]
for i in range(n):
    trans.append([])
    for j in range(m):
        trans[i].append(mat[j][i])
print'tranpose of the matrix:-'
for i in range(m):
    for j in range(n):
        print trans[i][j],
    print
