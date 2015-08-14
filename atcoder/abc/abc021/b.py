N = int(raw_input())
a, b = map(int, raw_input().split())
K = int(raw_input())
P = map(int, raw_input().split())+[a,b]
print "YES" if len(P) == len(set(P)) else "NO"
