def bk(k):
    global sol,n,s
    for i in range(1,n+1):
        sol[k]=i
        s+=i
        if sol[k]>=sol[k-1] and s<=n:
            if s==n:
                print(sol)
            else:
                bk(k+1)
        s-=i
        sol[k]=0
n=int(input())
sol=[0]*(n+1)
s=0
bk(1)