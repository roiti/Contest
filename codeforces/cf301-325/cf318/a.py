def gcd(a, b):
    while b: a, b = b, a % b
    return a

def lca(a, b):
    return a / gcd(a, b) * b

n = int(raw_input())
a = map(int, raw_input().split())

g = reduce(lambda x, y: gcd(x, y), a)
for i in a:
    i /= g
    for j in [2, 3]:
        while i % j == 0:
            i /= j
    if i != 1:
        print "No"
        break
else:
    print "Yes"
