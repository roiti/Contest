def gcd(a,b):
    while b: a,b = b,a%b
    return a
    
N = int(raw_input())
K = int(raw_input())
s = range(N)
for loop in xrange(K):
    X,Y = map(int,raw_input().split())
    X -= 1; Y -= 1
    s[X],s[Y] = s[Y],s[X]

step = [1]*N
for i in range(N):
    p = s[i]
    while p != i:
        p = s[p]
        step[i] += 1
        
print reduce(lambda a,b:a*b/gcd(a,b), step)