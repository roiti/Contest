#include <stdio.h>
int main(){
	int i,a[26]={};
	char w;
	while (scanf("%c",&w)!=EOF){
		if (w>='a'&&w<='z')
			a[w-'a']++;
		else if (w>='A'&&w<='Z')
			a[w-'A']++;
	}
	for (i=0;i<26;i++)
		printf("%c : %d\n",i+'a',a[i]);	
	return 0;
}

