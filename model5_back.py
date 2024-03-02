def bk(k):
    global s, p, n
    for v in range(s[k-1], (p//2)+1):
        s[k] = v
        if sum(s) == p:
            n += 1
            print(s)
        else:
            bk(k+1)
        s[k]=0

p = int(input())
s = [0] * (p+1)
s[0] = 1
n = 0
bk(1)
print(n)
