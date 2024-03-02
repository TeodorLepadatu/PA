def drojdie(k):
    global sol
    if k==1:
        return True
    else:
        if abs(sol[k]-sol[k-1])!=1:
            return False
        return True

def bk(k):
    global sol, A, B, n
    for c in range(0, 10):
        sol[k] = c
        n = n * 10 + c
        if drojdie(k):
            if A <= n and n <= B:
                print(n)
            else:
                bk(k + 1)
        sol[k] = 0
        n = (n - c) // 10

date = [int(x) for x in input().split()]
A = date[0]
B = date[1]
sol = [0] * 10
n = 0
bk(1)
