#include <stdio.h>
#include <string.h>

int main(void) {
	int i,size,m,h;
	char c[200],cc[200];
	
	while (1){
		scanf("%s",&c);
		if (c[0]=='-') break;
		
		size=strlen(c);
		scanf("%d",&m);
		while (m--){
			scanf("%d",&h);
			for (i=0;i<h;i++){
				cc[i]=c[i];
			}
			for (i=h;i<size;i++){
				c[i-h]=c[i];
			}
			for (i=0;i<h;i++){
				c[i+size-h]=cc[i];
			}
		}
		printf("%s\n",c);
	}
  return 0;
}

