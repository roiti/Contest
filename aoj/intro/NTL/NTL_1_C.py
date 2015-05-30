def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n = int(raw_input())
a = map(int, raw_input().split())
l = a[0]

for i in range(1,len(a)):
    b = a[i]
    g = gcd(l, b)
    l = l * b / g
print l
