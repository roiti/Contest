#include <stdio.h>
#include <math.h>
#define PI 3.141592653589

int main(){
	double a,b,c,C,h,S,L;
	scanf("%lf %lf %lf",&a,&b,&C);
	h=b*sin(C/180*PI);
	S=a*h/2;
	c=sqrt(pow(a,2)+pow(b,2)-2*a*b*cos(C/180*PI));
	printf("%lf\n%lf\n%lf",S,a+b+c,h);
	return 0;
}	

