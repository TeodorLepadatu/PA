def diferenta(k):
    global sol
    for cif in range(k-1,-1,-1):
        if abs(sol[k]-sol[cif])>p:
            return False
    return True

def bk(k):
    global p,c,sol,s
    for i in range(1,10):
        sol[k]=i
        s+=i
        if s<=c:
            if s==c:
                if diferenta(k) and sol[0]==sol[k]:
                    print(sol)
            else:
                bk(k+1)
        sol[k]=0
        s-=i


p=int(input())
c=int(input())
sol=[0]*c
s=0
bk(0)