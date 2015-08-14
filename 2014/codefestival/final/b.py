import math,string,random,itertools,bisect
inf = 0x10101010
pi = math.pi
# Functions
########################################################
 
 
# main procedure
########################################################
S = raw_input()
ans = 0
for i in range(len(S)):
    if i%2 == 0:
        ans += int(S[i])
    else:
        ans -= int(S[i])
print ans
