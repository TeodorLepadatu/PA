def numere(*x):
    d={}
    num=[]
    for n in x:
         num.append(n)
    num=sorted(num)
    for n in num:
        cn=n
        s=0
        k=0
        while cn!=0:
            s+=(cn%10)
            cn//=10
            k+=1
        av=s/k
        if av not in d.keys():
            aux={av:[n]}
            d.update(aux)
        else:
            d[av].append(n)
    d=dict(sorted(d.items()))
    return d
L=[x for x in range(100,1000)]
m=int(input())
n=int(input())
a=[]
maxim=[]
minim=[]
for i in range(0,m):
        v=[float(x) for x in input().split()]
        maxim.append(max(v))
        minim.append(min(v))
        a.append(v)
s=0
sol=[]
mx=0
ok=1
elem=0
for i in range(0,m):
    minc=999999999
    for j in range(0,n):
        if i==0:
            elem=minim[i]
            mx=elem
        elif i!=m-1:
            if maxim[i]<minim[i+1]:
                ok=0
            else:
                if a[i][j]>mx and a[i][j]<minc:
                    elem=a[i][j]
                    mx=elem
                    minc=a[i][j]
                else:
                    elem=a[i][j]
        else:
            elem=maxim[i]
    s+=elem
    print(elem)
if ok==0:
    print("Imposibil")
else:
    print(s)
#cel mai mic care e mai mare decat pe cel pe care l am ales la linia de dinainte si e mai mare ca minimul din linia urm