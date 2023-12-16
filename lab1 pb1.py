n=int(input())
nou=0
c=n
while n!=0:
    nou=nou*10+n%10
    n=n//10
if c==nou:
    print("palindrom")
else:
    print("nu e palindrom")