B=[int(x) for x in input().split()]
S=int(input())
sol=[]
while S!=0:
    if S%B[len(B)-1]!=0 and S%B[len(B)-2]!=0 and S>B[len(B)-2] and (S-B[len(B)-2])%B[len(B)-3]!=0:
        if S>=B[len(B)-1]:
            sol.append(B[len(B)-1])
            S-=B[len(B)-1]
        elif S<B[len(B)-1] and S>=B[len(B)-2]:
            sol.append(B[len(B)-2])
            S-=B[len(B)-2]
    elif S%B[len(B)-1]==0:
        while S!=0:
            sol.append(B[len(B)-1])
            S-=B[len(B)-1]
    elif S%B[len(B)-2]==0:
        while S!=0:
            sol.append(B[len(B)-2])
            S-=B[len(B)-2]
    elif (S-B[len(B)-2])%B[len(B)-3]==0:
        sol.append(B[len(B)-2])
        S-=B[len(B)-2]
    else:
        i=len(B)-3
        while S!=0:
            while S>=B[i]:
                sol.append(B[i])
                S-=B[i]
            i-=1
print(sol)