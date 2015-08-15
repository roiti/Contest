from collections import defaultdict
 
n = int(raw_input())
a = [raw_input() for i in xrange(n)]
cnt = [0]*n
sa = set(a)
val = defaultdict(int)
for i in xrange(n):
    ai = a[i]
    for j in xrange(9):
        nai = ai[:j]+ai[j+1]+ai[j]+ai[j+2:]
        if nai == ai: continue
        if nai in sa:
            cnt[i] += 1
 
ac = sorted(zip(a,cnt), key = lambda x:x[1], reverse = True)
for ai,c in ac:
    used = [0]*9
    for j in xrange(9):
        nai = ai[:j]+ai[j+1]+ai[j]+ai[j+2:]
        if nai == ai: continue
        if nai in sa:
            used[val[nai]] = 1
    for j in xrange(9):
        if used[j] == 0:
            val[ai] = j
            break
 
d = min(val[ai] for ai in a)
for ai in a:
    print val[ai]-d
