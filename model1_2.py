def valid(lista, index, k):
    for i in range(1, index):
        if abs(lista[i] - lista[index]) > k:
            return False
    return True

def bk(x):
    global s,g,n,k
    for v in range(1, g + 1):
        s[x] = v
        if valid(s,x,k):
            if x == n:
                if sum(s)==g:
                    print(s)
            else:
                bk(x + 1)

g = int(input("Enter g: "))
n = int(input("Enter n: "))
k = int(input("Enter k: "))
s = [0] * (n+1)
print(s)
bk(1)

