m=[[1,2,3],[4,5,6],[7,8,9],]
numere=[m[i][i]**2 for i in range(len(m))]
def f(lista):
    global pasi
    pasi+=1
    if len(lista) <= 2:
        return min(lista)
    k = len(lista) // 2
    aux_1 = lista[:k]
    aux_2 = lista[k+1:]
    return min(f(aux_1), lista[k])
pasi=0
f([1,2,3,4,5,6,7,8,9,10,11,12])
print(pasi)