v=[int(x) for x in input().split()]
sol=[1]
i=0
while i<len(v):
    mx=0
    next=i
    if len(v)-(i+1)<=v[i]:
        sol.append(len(v))
        break
    for index in range(i+1,i+v[i]+1):
        if v[index]>mx:
            next=index
            mx=v[index]
    sol.append(next+1)
    i=next
print(sol)