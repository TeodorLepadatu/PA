def bk(k):
    global n,m,sol
    for i in range(1,n+1):
        sol[k]=i
        if sol[k] not in sol[:k]:
            if k==m:
                print(*sol[1:])
            else:
                bk(k+1)
        sol[k]=0
n=int(input())
m=int(input())
sol=[0]*(m+1)
bk(1)