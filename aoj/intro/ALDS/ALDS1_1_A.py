def isort(n,a):
    print " ".join(map(str, a))
    for j in range(1,n):
        key = a[j]
        i = j-1
        while i >= 0 and a[i] > key:
            a[i+1] = a[i]
            i = i - 1
        a[i+1] = key
        print " ".join(map(str, a))

n = int(raw_input())
a = map(int, raw_input().split())
isort(n,a)

