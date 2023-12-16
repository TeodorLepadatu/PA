L1=int(input())
L2=int(input())
S=L1*L2
l=0
while L2:
    l=L1%L2
    L1=L2
    L2=l
n=S//(L1**2)
print(f"latura={L1} si numarul de placi este {n}")