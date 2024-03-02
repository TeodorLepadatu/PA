def f(lista, p, u):
    global pasi
    pasi+=1
    if u - p <= 1:
        return lista[p]
    k = (p + u) // 2
    if k % 2 == 0:
        return f(lista, p, k-2) + f(lista, k+2, u)
    else:
        return f(lista, p, k-1) + f(lista, k+1, u)
pasi=0
L=[x for x in range(0,10000001)]
f(L, 0, 10000000)
print(pasi)