n,q = map(int, raw_input().split())
que = [map(str, raw_input().split()) for i in range(n)]
for i in range(n):que[i][1] = int(que[i][1])
mxt = sum([y for x,y in que])
t = 0
i = 0
while t < mxt:
    if i >= n: i %= n
    if que[i][1] <= q:
        t += que[i][1]
        print que[i][0],t
        que.pop(i)
        n -= 1
    else:
        t += q
        que[i][1] -= q
        i += 1

