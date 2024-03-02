L=[int(x) for x in input().split()]
C=[int(x) for x in input().split()]
d = {L[i]: (i, C[i]) for i in range(len(L))}
print(d)
F=[]
L=sorted(d,reverse=True)
F.append(d[L[0]][0])
for j in range(1,len(L)):
    if d[L[j]][1]!=d[L[j-1]][1]:
        F.append(d[L[j]][0])
print(F)
print(len(F))