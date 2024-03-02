def bk(k):
    global sol,m,n
    for i in range(1,n+1):
        sol[k]=i
        if sol[k]>sol[k-1]:
            if k==m:
                print(*sol[1:])
            else:
                bk(k+1)
        sol[k]=0
n=int(input())
m=int(input())
sol=[0]*(m+1)
bk(1)