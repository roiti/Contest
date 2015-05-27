alpha = "abcdefghijklmnopqrstuvwxyz"
hist = [0]*26
n = int(raw_input())
s = raw_input().lower()
for i in s:
    hist[alpha.index(i)] += 1
print "YES" if min(hist) > 0 else "NO"
