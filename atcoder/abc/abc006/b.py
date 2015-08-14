a = [0]*1000010
a[2] = 1
N = int(raw_input())
for i in xrange(3,N):
    a[i] = (a[i-1]+a[i-2]+a[i-3])%10007
print a[N-1]
