#include <stdio.h>
int main(){
  int r,c,i,j,sum,s[101][101];
  scanf("%d %d", &r, &c);
  for (i = 0; i < r; i++){
    sum=0;
    for (j = 0; j < c; j++){
      scanf("%d",&s[i][j]);
      sum+=s[i][j];
    }
    s[i][c]=sum;
  }
  for (j = 0; j < c+1; j++){
    sum = 0;
    for (i = 0; i < r; i++)
      sum += s[i][j];
    s[r][j]=sum;
  }
  for (i = 0; i < r+1; i++){
    for (j= 0; j < c+1; j++){
      printf("%d",s[i][j]);
      if (j!=c) printf("%s"," ");
    }
    printf("%s","\n");
  }
  return 0;
}

