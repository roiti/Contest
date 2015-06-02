int main(){
	char op;
	int a,b;
	while (1){
		scanf("%d %c %d",&a,&op,&b);
		if      (op=='?') break;
		else if (op=='+') printf("%d\n",a+b);
		else if (op=='-') printf("%d\n",a-b);
		else if (op=='*') printf("%d\n",a*b);
		else if (op=='/') printf("%d\n",a/b);
	}
	return 0;
}

