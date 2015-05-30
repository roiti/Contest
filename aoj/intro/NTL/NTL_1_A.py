n = m = int(raw_input())
r = int(math.sqrt(n))
sqrt = int(math.sqrt(r))
p = [1]*r
p[0] = 0
for i in range(1,sqrt):
    if p[i]:
        p[2*i+1::i+1] = [0 for x in range(2*i+1,r,i+1)]

prime=[]
for i in range(r):
    if p[i]:
        prime.append(i+1)

a = []
for i in range(len(prime)):
    if n % prime[i] == 0:
        j = prime[i]
        while n % j == 0:
            n /= j
            a.append(j)
if n == m:
    print str(m)+":",m
elif n != 1:
    print str(m)+":"," ".join(map(str, a)),n
else:
    print str(m)+":"," ".join(map(str, a))
