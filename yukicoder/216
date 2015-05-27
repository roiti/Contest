N = input()
a = map(int, raw_input().split())
b = map(int, raw_input().split())
score = [0] * 110
for i in xrange(N):
    score[b[i]] += a[i]
if max(score) == score[0]:
    print "YES"
else:
    print "NO"