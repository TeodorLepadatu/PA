n=int(input())
p=int(input())
mx=mn=p
for i in range (1,n):
    c=int(input())
    mn=min(c,mn)
    mx=max(c,mx)
    p=c
print(mn,mx)