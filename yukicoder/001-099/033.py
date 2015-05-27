N,D,T = map(int,raw_input().split())
A = {}
X = map(int,raw_input().split())
for x in X:
    if x%D not in A: A[x%D] = [[x/D-T, x/D+T]]
    else: A[x%D].append([x/D-T,x/D+T])

A = [sorted(a) for a in A.values()]
ans = 0
for a in A:
    a0 = a[0]
    for ai in a[1:]:
        if a0[1] >= ai[0]: a0[1] = max(a0[1],ai[1])
        else: 
            ans += a0[1]+1-a0[0]
            a0 = ai
    ans += a0[1]+1-a0[0]
print ans