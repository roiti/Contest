#include <stdio.h>
int main(){
	int i;
	char c[1201];
	gets(c);
	for (i=0;i<1201;i++){
		if (c[i]>='a'&&c[i]<='z')
			c[i]=c[i]-32;
		else if (c[i]>='A'&&c[i]<='Z')
			c[i]=c[i]+32;
	}
	printf("%s\n",c);
	return 0;
}

