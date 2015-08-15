n, x = map(int, raw_input().split())
x -= 1
h = map(int, raw_input().split())

tree = [[] for i in xrange(n)]
for loop in xrange(n - 1):
    a, b = map(int, raw_input().split())
    a -= 1; b -= 1
    tree[a].append(b)
    tree[b].append(a)

node = n
while 1:
    change = False
    for i in xrange(n):
        if h[i] == 1 or i == x: continue
        if len(tree[i]) == 1:
            a = tree[i][0]
            tree[a].remove(i)
            tree[i] = []
            node -= 1
            change = True
    if not change: break
print (node - 1) * 2
