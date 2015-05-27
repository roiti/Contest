Sum,Limit = map(int,raw_input().split())
k = [0]*30
klist = [[] for i in range(30)]
for i in range(Limit,0,-1):
    idx = format(i,"b")[::-1].index("1")
    k[idx] += 1
    klist[idx].append(i)

ans = []
idx = k.index(0)-1
while Sum > 0:
    if k[idx] > 0 and Sum - 2**idx >= 0:
        k[idx] -= 1
        Sum -= 2**idx
        ans.append(klist[idx].pop())
    else:
        if idx == 0:
            break
        else:
            idx -= 1
if Sum == 0:
    print len(ans)
    print " ".join(map(str,ans))
else:
    print -1
