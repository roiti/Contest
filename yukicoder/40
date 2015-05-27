D = int(raw_input())
b = map(int,raw_input().split())
for i in range(3,D+1)[::-1]:
    b[i-2] += b[i]
    b[i] = 0
for i in range(D+1)[::-1]:
    if b[i] != 0 or i == 0:
        print i
        print " ".join(map(str,b[:i+1]))
        break