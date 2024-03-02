def valid(k):
    global sol
    for i in range(k-1,-1,-1):
        if sol[k]==sol[i]:
            return False
    return True
def bk(k):
    global n,t,L,S,ok,rez
    rez=""
    if t[k]=="l":
        for c in L:
            sol[k]=c
            if valid(k):
                if k==len(t)-1:
                    ok=1
                    for i in sol:
                        rez+=i
                    if rez[0] in "aeiouAEIOU":
                        print(rez)
                else:
                    bk(k+1)
            sol[k]=0
    else:
        for c in S:
            sol[k]=c
            if valid(k):
                if k==len(t)-1:
                    ok=1
                    for i in sol:
                        rez+=i
                    if rez[0] in "aeiouAEIOU":
                        print(rez)
                else:
                    bk(k+1)
            sol[k]=0
n=int(input())
t=input()
L=input().split()
S=input().split()
sol=[0]*n
ok=0
bk(0)
if ok==0:
    print("Imposibil")