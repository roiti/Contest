na,nb = map(int,raw_input().split())
a = set(map(int,raw_input().split()))
b = set(map(int,raw_input().split()))
print len(a&b)*1.0/len(a|b)
