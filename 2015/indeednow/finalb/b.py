N = int(raw_input())
inroom = []
people = [0]*(2*N+10)
 
st = [map(int,raw_input().split()) for i in xrange(N)]
for s,t in st:
    people[s] += 1
 
for i in xrange(1,2*N+10):
    people[i] += people[i-1]
 
for s,t in st:
    print people[t]-people[s]
