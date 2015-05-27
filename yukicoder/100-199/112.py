N = int(raw_input())
a = map(int,raw_input().split())
s = sum(a)/(N-1)
print (4*N-s)/2,(s-2*N)/2
