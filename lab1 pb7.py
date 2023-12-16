n=int(input())
p=int(input())
c=int(input())
rez=p^c
for i in range (2,n):
    c=int(input())
    rez=rez^c
print(rez)