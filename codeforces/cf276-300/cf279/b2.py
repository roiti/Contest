n = int(raw_input())
id = [map(int,raw_input().split()) for _ in range(n)]
nxt = {a:b for a,b in id}
que = [0]*n
b = nxt[0]
que[1] = b
for i in range(3,n,2):
    b = nxt[b]
    que[i] = b

sa,sb = set(a for a,b in id),set(b for a,b in id)
sp = list(sa-sb)[0]
if n > 2:
    a,b = sp,nxt[sp]
    que[0],que[2] = a,b
    for i in range(4,n,2):
        b = nxt[b]
        que[i] = b
else:
    que[0] = sp
print " ".join(map(str,que))
