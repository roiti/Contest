N = int(raw_input())
M = int(raw_input())
m = M
while m%2 == 0: m /= 2
while m%5 == 0: m /= 5
if N%M == 0:
    a = N/M
    while a%10 == 0: a /= 10
    print str(a)[-1]
elif m == 1:
    a = 10**1000/M*N
    while a%10  == 0: a /= 10
    print str(a)[-1]
else:
    print -1
