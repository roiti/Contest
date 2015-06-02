#include <stdio.h>

int main(void) {
	int i,j,p,n,num,c[4][13]={0};
	char s[2],ref[]="SHCD";
	scanf("%d",&n);
	while (n--){
		scanf("%s %d",&s,&num);
		if (s[0]=='S') p=0;
		if (s[0]=='H') p=1;
		if (s[0]=='C') p=2;
		if (s[0]=='D') p=3;
		c[p][num-1]=1;
	}
	for (i=0;i<4;i++){
		for (j=0;j<13;j++){
			if (c[i][j]==0){
				printf("%c %d\n",ref[i],j+1);
			}
		}
	}
	return 0;
}

