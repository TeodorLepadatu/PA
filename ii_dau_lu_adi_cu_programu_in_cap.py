f=[0,1]
i=1
while(f[i-1]<=500):
    if i==1:
        f[i]=1
        i+=1
    elif i%2==0:
        f.append((f[i-1]*2)+2)
        i+=1
    else:
        f.append(f[i-1]+1)
        i+=1
print(f)
x=int(input())
ok=0
if x%2==0:
    if x%4==0:
        p=x//4
        p+=1
        for k in range(0,10):
            if 2**k==p:
                ok=1
else:
    x1=x-1
    if x1%2==0:
        if x1%4==0:
            p=x1//4
            p+=1
            for k in range(0,10):
                if 2**k==p:
                    ok=1
print(ok)

#f(n)=1, n==1
#f(n)=2*f(n-1)+2, n=par
#f(n)=f(n-1)+1, n=impar


