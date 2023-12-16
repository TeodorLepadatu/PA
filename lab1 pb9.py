'''n=int(input())
k=int(input())
b=int(input())
c=n>>(k-1)
if c%2==1 & b==0:
    c=c-1
elif c%2==0 & b==1:
    c=c+1
elif c%2==0 & b==0:
    pass
else:
    pass
c=c<<(k-1)
c=c+(n%(2**(k-1)))
print(c)'''
def set_bit(n, k, b):
    # Pentru a seta al k-lea bit la 1, folosim un operator OR cu un număr format doar din biti 0 si un bit 1 la pozitia k
    if b == 1:
        return n | (1 << k)
    # Pentru a seta al k-lea bit la 0, folosim un operator AND cu un număr format din biti 1 cu un bit 0 la pozitia k
    else:
        return n & ~(1 << k)

# Citim numerele n, k și valoarea binară b
n = int(input("Introduceți numărul n: "))
k = int(input("Introduceți poziția k: "))
b = int(input("Introduceți valoarea binară (0 sau 1): "))

# Apelăm funcția set_bit pentru a efectua operația
rezultat = set_bit(n, k, b)

print(f"Numărul rezultat după setarea bitului {k} la {b} este: {rezultat}")