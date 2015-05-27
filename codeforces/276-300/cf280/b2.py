n,l = map(int,raw_input().split())
if n > 1:
    a = sorted(map(int,raw_input().split()))
    d = max(aj-ai for ai,aj in zip(a[:-1],a[1:]))/2.0
    if a[0] != 0: d = max(d,a[0])
    if a[-1]!= l: d = max(d,l-a[-1])
else:
    a = int(raw_input())
    d = max(a,l-a)
print d
