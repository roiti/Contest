#include <stdio.h>
#include <math.h>

int main(){
	int i,n;
	double ave,alpha,s[1001];
	while (1){
		scanf("%d",&n);
		if (n==0) break;
		ave=0.0;
		for (i=0;i<n;i++){
			scanf("%lf",&s[i]);
			ave+=s[i];
		}
		ave/=n;
		alpha=0.0;
		for (i=0;i<n;i++){
			alpha+=pow(s[i]-ave,2);
		}
		printf("%lf\n",sqrt(alpha/n));
	}
	return 0;
}

