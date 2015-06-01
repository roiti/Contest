def bubble(n, a):
    count = 0
    for i in range(n-1):
        for j in range(n-1,i,-1):
            if a[j-1] > a[j]:
                tmp = a[j]
                a[j] = a[j-1]
                a[j-1] = tmp
                count += 1
    return count, a
    
n = int(raw_input())
a = map(int, raw_input().split())

n, a = bubble(n, a)
print " ".join(map(str, a))
print n

