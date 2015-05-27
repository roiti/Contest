import itertools as it
def gcd(a,b):
    while b: a,b = b,a%b
    return a
    
l,r = map(int,raw_input().split())
for a,b,c in it.combinations(range(l,r+1),3):
    if gcd(a,b) == 1 and gcd(b,c) == 1 and gcd(c,a) > 1:
        print " ".join(map(str,sorted([a,b,c])))
        break
else:
    print -1
