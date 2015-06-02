r, c = map(int, raw_input().split())
sum_c = [0 for x in range(r)]
sum_r = [0 for x in range(c)]
sum = 0

for i in range(r):
    column = map(int, raw_input().split())
    for j in range(c):
        sum_c[i] += column[j]
        sum_r[j] += column[j]
        sum += column[j]
    print(" ".join(map(str, column)) + " " + str(sum_c[i]))

print (" ".join(map(str, sum_r)) + " " + str(sum))

