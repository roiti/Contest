N, K = map(int, raw_input().split())    
l = sorted(map(int, raw_input().split()))
print sum(l[-K:])

