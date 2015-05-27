mod = 10**9+7
n = int(raw_input())
dna = raw_input()

cnt = sorted([dna.count("A"),dna.count("G"),dna.count("C"),dna.count("T")])[::-1]
num = cnt.count(cnt[0])

ans = 1
for i in xrange(n):
    ans = ans * num % mod

print ans
