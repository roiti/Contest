n = input()
s = set(range(1,n+1))
a = set(map(int,raw_input().split()))
print list(s-a)[0]
