a=int(input())
b=int(input())
f1=0
f2=1
f3=f1+f2
while a>f3:
    f1=f2
    f2=f3
    f3=f1+f2
    if f3>b:
        break
if f3<=b:
    print(f3)
else:
    print("nu exista")