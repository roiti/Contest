n,r,avg = map(int,raw_input().split())
need = n*avg
ab = [map(int,raw_input().split()) for _ in range(n)]
ab = sorted(ab,key = lambda x:x[1])
now = sum(a for a,b in ab)
ans = 0
for a,b in ab:
    if now >= need: break
    ans += min(need-now,r-a)*b
    now += min(need-now,r-a)
print ans
