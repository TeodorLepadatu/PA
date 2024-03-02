n=int(input())
g=float(input())
d={}
for i in range(1,n+1):
    x=float(input())
    d[x]=i
v=d.keys()
v=sorted(v)
print(d)
print(v)
st=0
dr=1
cnt=0
sol=[]
while dr<len(v) and st<len(v):
    if st==dr:
        dr+=1
    else:
        if v[dr]-v[st]<=g:
            if v[dr] in d.keys() and v[st] in d.keys():
                sol.append((d[v[st]],d[v[dr]]))
                d.pop(v[dr])
                d.pop(v[st])
                cnt+=1
                dr+=1
            elif v[dr] not in d.keys() and v[st] not in d.keys():
                dr+=1
                st+=1
            elif v[dr] not in d.keys():
                dr+=1
            else:
                st+=1
        else:
            st+=1
print(cnt)
for e in sol:
    print(f"{e[0]} + {e[1]}")