n=int(input())
mx=0
p=float(input(""))
zi=0
for i in range (1,n):
    c=float(input())
    if mx<abs(p-c):
        zi=i
    mx=max(mx,round(abs(p-c),2))
    p=c
print(f"cea mai mare crestere a fost de {round(mx,2)} RON si a fost ingresitrata intre zilele {zi} si {zi+1}")
