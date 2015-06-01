inf = 10**9
N = int(raw_input())
p = [int(raw_input()) for i in xrange(N)]
to = [i for i in xrange(N)]
for i in xrange(N):
        if to[i] != i: continue
        seq = set([])
        while 1:
            if to[i] != i:
                for j in seq: to[j] = to[i]
                break
            elif i in seq:
                for j in seq: to[j] = -1
                break
            elif p[i] == 0:
                for j in seq: to[j] = i
                break
            else:
                seq.add(i)
                i += p[i]

visited = [False]*N
visited[0] = True
que = [[0,0]]
while 1:
    cur,step = que.pop(0)
    if cur == N-1:
        print step
        break
    for nxt in range(cur+1,min(N,cur+7)):
        if to[nxt] > 0 and not visited[to[nxt]]:
            visited[to[nxt]] = True
            que.append([to[nxt], step+1])


