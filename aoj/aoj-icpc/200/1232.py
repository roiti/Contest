import bisect
R = 100001/2
p = [1]*R
p[0] = p[1] = 0
for i in range(2,int(R**0.5)+1):
    if p[i]:
        p[2*i::i] = [0]*len(p[2*i::i])
p = [i for i in range(R) if p[i]]
n = len(p)
pxp = []
for i in range(n):
    for j in range(i,n):
        if p[i]*p[j] > 100000: break
        pxp.append([p[i]*p[j],p[i],p[j]])
pxp = sorted(pxp)
p,xyr = [e[0] for e in pxp],[[e[1],e[2],e[1]*1.0/e[2]] for e in pxp]
while 1:
    m,a,b = map(int,raw_input().split())
    if m == 0: break
    ab = a*1.0/b

    sp = bisect.bisect(p,m)
    for i in range(sp)[::-1]:
        if 1 >= xyr[i][2] >= ab:
            print xyr[i][0],xyr[i][1]
            break

