import bisect
N = int(raw_input())
s = [int(raw_input()) for i in xrange(N)]
num = [0]*1000010
for si in s:
    if si > 0:
        num[0] += 1
        num[si+1] -= 1
for i in xrange(1,1000010):
    num[i] += num[i-1]
num = num[::-1]
 
Q = int(raw_input())
for loop in xrange(Q):
    k = int(raw_input())
    print abs(bisect.bisect(num,k)-1000010)
