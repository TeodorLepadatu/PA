def bk(k):
    global m,sol,afis
    for i in m:
        sol[k]=i
        if k==len(m)-1:
            print(set(sol))
        else:
            bk(k+1)
        sol[k]=0
m=set([int(x) for x in input().split()])
sol=[0]*len(m)
afis=[]
bk(0)