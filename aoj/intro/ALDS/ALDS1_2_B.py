n = int(raw_input())
a = map(int, raw_input().split())
count = 0
for i in range(n):
    mini = i
    for j in range(i,n):
        if a[j] < a[mini]:
            mini = j
    if i != mini:
        a[i], a[mini] = a[mini], a[i]
        count += 1
print " ".join(map(str, a))
print count


