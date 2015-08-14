n = int(raw_input())
p = set(map(int,raw_input().split())[1:])
q = set(map(int,raw_input().split())[1:])
pq = sorted(list(p|q))
if pq == [i for i in range(1,n+1)]:
    print "I become the guy."
else:
    print "Oh, my keyboard!"
