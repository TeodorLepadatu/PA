n=int(input())
s=(n*(n+1))//2
for i in range (1,n):
    c=int(input())
    s=s-c
print(s)