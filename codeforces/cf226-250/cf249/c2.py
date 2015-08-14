n = input()
a = map(int,raw_input().split())
L = sum(a)
h = maxh = minh = 1000
A = [[" "]*L for i in range(2001)]
i = 0
sign = 1
for ai in a:
    if sign == 1:
        for j in range(ai):
            A[h+j][i+j] = "/"
        maxh = max(maxh,h+(ai-1))
        h += ai-1
    else:
        for j in range(ai):
            A[h-j][i+j] = "\\"
        minh = min(minh,h-(ai-1))
        h -= ai-1
    i += ai
    sign *= -1
for hi in range(maxh,minh-1,-1):
    print "".join(A[hi])
