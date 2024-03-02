L=[x for x in range(1000,10000) if x%10==x//1000 and (x//10)%10==(x//100)%10]
print(L)