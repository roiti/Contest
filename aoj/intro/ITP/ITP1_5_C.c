int main(){
	int h,w,hi,wi;
	while (1){
		scanf("%d %d",&h,&w);
		if (h == 0) break;
		for (hi=0; hi<h; hi++){
			for (wi=0; wi<w; wi++)
				printf((hi+wi)%2==0 ? "#":".");
			printf("\n");
		}
		printf("\n");
	}
	return 0;
}

