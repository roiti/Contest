#include <stdio.h>
int main(){
	int a,b,tmp;
	while (1){
		scanf("%d %d",&a,&b);
		if (a==0 && b==0)
			break;
		if (a>b){
		tmp=a;a=b;b=tmp;
		}
		printf("%d %d\n",a,b);
	}
	return 0;
}

