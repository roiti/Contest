N,K = map(int,raw_input().split())
s = raw_input()
a = 0
for i in (range(K-1,N) if s[K-1] == "(" else range(K)[::-1]):
    a += 1 if s[i] == "(" else -1
    if a == 0:
        print i+1
        break