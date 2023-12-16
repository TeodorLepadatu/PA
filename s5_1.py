M=[[7, 10, 14, 21], [10, 15, 18, 22], [14, 23, 32, 41], [41, 43, 51, 71], [66, 70, 75, 90]]
def a(M):
    for l in M:
        l=sorted(l)
    for c in zip(*M):
        c=tuple(sorted(c))
    return M
def b1(x,m,n):
    for i in range(0,m):
        for j in range(0,n):
            if M[i][j]==x:
                return (i,j)
    return None
def b2(x,M):
    m=len(M[0])
    for i in range(0,m):
        s=0
        d=len(M[i])-1
        while s<=d:
            mij=(s+d)//2
            if M[i][mij]==x:
                return (i,mij)
            elif M[i][mij]<x:
                s=mij+1
            else:
                d=mij-1
    return None
def b3(x,M):
    m=len(M)  
    n=len(M[0])  
    i=0
    j=n-1
    while i<m and j>=0:
        if M[i][j]==x:
            return i, j  
        elif M[i][j]>x:
            j-=1  
        else:
            i+=1  
    return None  