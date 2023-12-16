n=int(input())
cif=[0,0,0,0,0,0,0,0,0,0]
mx=mn=0
while n:
    cif[n%10]+=1
for i in range (9,-1,-1):
    j=1
    while j<=cif[i]:
        mx=mx*10+i
        j+=1
print(mx)