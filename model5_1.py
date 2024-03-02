def aparitii(*x):
    d = {}
    for n in x:
        if n not in d.keys():
            cn = n
            l = []
            t = []
            while cn != 0:
                cif = cn % 10
                found = False
                for i in range(0, len(t), 2):
                    if t[i] == cif:
                        t[i + 1] += 1
                        found = True
                        break
                if not found:
                    t.append(cif)
                    t.append(1)
                cn //= 10
            for i in range(0, len(t), 2):
                aux = (t[i], t[i + 1])
                l.append(aux)
            d.update({n: l})
    return d
N=int(input())
p=[int(x) for x in input().split()]
p=sorted(p,reverse=True)
s=0
while p!=[]:
    K=len(p)
    aux=p.pop()
    s+=(aux/(K+1))
s=round(s,3)
print(s)