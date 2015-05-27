N = int(raw_input())
bit = [format(i,"b").count("1") for i in xrange(1,N+1)]
step = [-1]*N
step[0] = 1
que = [[0,1]]
while que:
    i,cnt = que.pop(0)
    if i+bit[i] <  N and step[i+bit[i]] == -1:
        step[i+bit[i]] = cnt+1
        que.append([i+bit[i],cnt+1])
    if i-bit[i] > -1 and step[i-bit[i]] == -1:
        step[i-bit[i]] = cnt+1
        que.append([i-bit[i],cnt+1])
print step[N-1]