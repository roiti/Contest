import sys
H, W, Q = map(int, raw_input().split())
dist = [[0] * W for i in xrange(H)]
for h in xrange(H):
    for w in xrange(W):
        print 1, 1, h + 1, w + 1
        sys.stdout.flush()
        dist[h][w] = int(raw_input())
 
 
for query in xrange(Q):
    si, sj, ti, tj = map(int, raw_input().split())
    si -= 1; sj -= 1; ti -= 1; tj -= 1
    print dist[ti][tj] + dist[si][sj] - 2 * dist[min(si, ti)][min(sj, tj)]
    sys.stdout.flush()
