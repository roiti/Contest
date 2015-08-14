alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

N, M = map(int, raw_input().split())
name = raw_input()
kit = raw_input()
cnt = [kit.count(c) for c in alpha]

ans = 0
for i in xrange(len(alpha)):
    need = name.count(alpha[i])
    if need == 0: continue
    if need > 0 and cnt[i] == 0:
        ans = -1
        break
    ans = max(ans, (need + cnt[i] - 1) / cnt[i])
print ans
