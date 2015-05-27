n,m,k = map(int,raw_input().split())
army = [0]*(m+1)
for i in range(m+1):
    b = bin(int(raw_input()))[2:]
    b = ("0"*(n-len(str(b))) + str(b))
    army[i] = b

ans = 0
for i in range(m):
    count = 0
    for j in range(n):
        if army[i][j] != army[m][j]:
            count += 1
    if count <= k:
        ans += 1
print ans
