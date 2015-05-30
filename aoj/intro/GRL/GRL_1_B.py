inf = float("inf")
def bellman_ford(es, s):
    d[s] = 0
    for cnt in xrange(V):
        update = False
        for e in es:
            frm, to, cost = e
            if d[frm] != inf and d[to] > d[frm] + cost:
                d[to] = d[frm] + cost
                update = True
                if cnt == i - 1:
                    return True
    return False

V, E, r = map(int, raw_input().split())
es = [map(int, raw_input().split()) for i in xrange(E)]
d = [inf for i in xrange(V)]
negative = bellman_ford(es, r)
if negative:
    print "NEGATIVE CYCLE"
else:
    for i in d:
        if i < inf:
            print i
        else:
            print "INF"
