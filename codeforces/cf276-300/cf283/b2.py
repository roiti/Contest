n = int(raw_input())
d = map(int,list(raw_input()))
ans = "".join(map(str,d))
for m in range(n):
    d1 = d[m:]+d[:m]
    d1 = [(10-d1[0]+i)%10 for i in d1]
    ans = min(ans,"".join(map(str,d1)))
print ans
