f=lambda x:x if x==p[x]else f(p[x]);I=lambda:map(int,raw_input().split());N,Q=I();p=range(N+1)
while Q:A,B,C=sorted(map(f,I()));Q-=1;exec['p[C]=p[B]','print["YES","NO"][B<C]'][A]
