R,C,D = map(int,raw_input().split())
A = [map(int,raw_input().split()) for i in range(R)]
ans = 0
c = D%2
for y in range(R):
    for x in range(C):
    if (x+y)%2 == c and x+y <= D:
        ans = max(ans,A[y][x])
print ans
