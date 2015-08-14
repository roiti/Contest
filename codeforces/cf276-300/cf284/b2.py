n,m = map(int,raw_input().split())
dic = {}
for loop in xrange(m):
    a,b = raw_input().split()
    if len(a) <= len(b):
        dic[a] = a
        dic[b] = a
    else:
        dic[a] = b
        dic[b] = b
note = raw_input().split()
ans = [dic[word] for word in note]
print " ".join(ans)
