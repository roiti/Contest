#include <stdio.h>

int main(){
	int i,count=0;
	char w[11],m[101];
	scanf("%s",&w);
	while (1){
		scanf("%s",&m);
		if (strcmp("END_OF_TEXT",m)==0) break;
		for (i=0;i<101;i++){
			if (m[i]>='A'&&m[i]<='Z')
				m[i]=m[i]+32;
		}
		if (strcmp(w,m)==0) count++;
	}
	printf("%d\n",count);
	return 0;
}	

