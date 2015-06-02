#include <stdio.h>
int main(){
	int i,sum;
	char c[1001];
	while (1){
		gets(c);
		if (c[0]=='0') break;
		sum=0;
		for (i=0; c[i]>='0'&&c[i]<='9'; i++)
			sum += c[i]-'0';
		printf("%d\n", sum);
	}
	return 0;
}

