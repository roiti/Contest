a,b = map(int,raw_input().split())
print (b*(b-1)/2)*(a+b*a*(a+1)/2)%(10**9+7)
