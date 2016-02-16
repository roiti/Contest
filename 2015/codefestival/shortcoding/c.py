#s=lambda N:N/10+N%10+max([s(N/i)for i in range(2,99)if N%i<1]+[0]);print s(input())+
#s=lambda N:N/100+N/10%10+N%10+max([s(N/i)for i in range(2,99)if N%i<1]+[0]);print s(input())
s=lambda N:N/100+N/10%10+N%10+max([s(i)for i in range(1,N)if N%i<1]+[0]);print s(input())
