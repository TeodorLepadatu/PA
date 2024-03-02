def valid(s, n, k):
    for i in range(n - 1):
        for j in range(i + 1, n):
            if abs(s[i] - s[j]) > k:
                return False
    return True

def bk(x, G, n, k, s, result):
    if x == n:
        if valid(s, n, k) and sum(s)==G:
            result.append(list(s))
        return

    for v in range(1, G + 1):
        s[x] = v
        bk(x + 1, G, n, k, s, result)

G = int(input("Introduceți numărul de kilograme de aur (G): "))
n = int(input("Introduceți numărul de saci (n): "))
k = int(input("Introduceți valoarea k: "))

s = [0] * n
result = []

bk(0, G, n, k, s, result)

if result:
    print("Modalități de împărțire a aurului:")
    for sac in result:
        print(sac)
else:
    print("Imposibil")
