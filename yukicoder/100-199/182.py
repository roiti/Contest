from collections import defaultdict
N = int(raw_input())
A = map(int, raw_input().split())
histo = defaultdict(int)
for a in A:
    histo[a] += 1

ans = 0
for i in histo.values():
    if i == 1:
        ans += 1
print ans    