import math,string,random,itertools,bisect
inf = 0x10101010
pi = math.pi
# Functions
########################################################
 
 
# main procedure
########################################################
A = int(raw_input())
for k in range(11,10001):
    tmp = 0
    lk = len(str(k))
    for i in range(lk):
        tmp += int(str(k)[i])*(k**(lk-i-1))
    if tmp == A:
        print k
        break
else:
    print -1
