def bkt(k):
    global s, n
    for v in range(1, n+1):
        s[k] = v
        if s[k] not in s[:k]:
            if k == m:
                print(*s[1:], sep=",")
            else:
                bkt(k+1)
n=int(input())
m=int(input())
s=[0]*m
bkt(1)