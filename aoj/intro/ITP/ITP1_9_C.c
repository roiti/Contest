#include <stdio.h>
#include <math.h>

int main(){
	int n,i,pt=0,ph=0;
	char ct[101],ch[101];
	scanf("%d",&n);
	for (i=0;i<n;i++){
		scanf("%s %s",&ct,&ch);
		if (strcmp(ct,ch)>0){
			pt+=3;
		}else if (strcmp(ct,ch)<0){
			ph+=3;
		}else{
			pt++;ph++;
		}
	}
	printf("%d %d\n",pt,ph);
	return 0;
}	

