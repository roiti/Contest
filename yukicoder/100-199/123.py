N,M = map(int,raw_input().split())
c = range(1,N+1)
for a in map(int,raw_input().split()):
    c = [c[a-1]]+c[:a-1]+c[a:]
print c[0]
