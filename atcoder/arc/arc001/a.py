N = int(raw_input())
c = map(int, list(raw_input()))
score = [0] * 4
for ci in c:
    score[ci - 1] += 1
print max(score), min(score)

