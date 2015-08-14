import bisect
N = int(raw_input())
H = map(int,raw_input().split())
if len(H) != len(set(H)):
    print -1
    exit()
 
sH = sorted(H)
ans = 0
for Hi in H:
    sH.remove(Hi)
    ans += sum(sH[:bisect.bisect(sH,Hi)])
print ans
