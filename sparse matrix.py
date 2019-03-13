m= input('enter the number of rows-')
n= input('enter the number of columns-')
print('enter matrix elements-')
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
sparse={}
for i in range(m):
    for j in range(n):
        if mat[i][j]!=0:
            sparse[(i,j)]= mat[i][j]
for i in sorted(sparse.keys()):
    print i,':',sparse[i]
        
    
