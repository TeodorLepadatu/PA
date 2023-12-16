f=open("autostrada.in.txt", "r")
g=open("autostrada.out.txt", "w")
l=int(f.readline())
v=[]
d={}
i=0
for linie in f.readlines():
    v+=[int(x) for x in linie.split()]
    d.update({v[i]:"("})
    d.update({v[i+1]:")"})
    i+=2
v=sorted(v)
stanga=0
dreapta=0
mn=0
mx=0
b=[]
avariat=0
for n in v:
    if stanga==dreapta:
        p=n
        mx=p
        b.append(mn)
        b.append(mx)
    if d[n]=="(":
        stanga+=1
    else:
        dreapta+=1
    if stanga==dreapta:
        stanga=0
        dreapta=0
        u=n
        mn=u
        dif=u-p
        avariat+=dif
        g.write(f"[{p},{u}]"+"\n")
b.append(u)
b.append(l)
for x in range(0,len(b),2):
    g.write(f"({b[x]},{b[x+1]})"+"\n")
uzura=round((avariat/l)*100)
g.write(f"{uzura}"+"%")
g.close
