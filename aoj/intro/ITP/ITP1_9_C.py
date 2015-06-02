score = [0, 0]

n = int(raw_input())
for i in range(n):
    t, h = raw_input().split()
    if t < h:
        score[1] += 3
    elif t > h:
        score[0] += 3
    else:
        score[0] += 1
        score[1] += 1
print score[0], score[1]

