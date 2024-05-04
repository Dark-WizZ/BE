#include <conio.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int getMat(int m, int n, int x[10][10]){
	for(int i=0;i<m;i++){
		for(int j=0; j<n; j++){
			char a[10];
			scanf("%s",&a);
			for(int c=0; c<strlen(a); c++){
				if(a[c]=='.') {
					printf("Test case 3: not int");
					return 1;
				}
			}
			x[i][j]=atoi(a);
		}
	}
	return 0;
}
int main(){
	int a[10][10],b[10][10],c[10][10];
	clrscr();
	printf("Size of matrix A: ");
	int m,n; scanf("%d%d",&m,&n);
	printf("Size of matrix B: ");
	int p, q; scanf("%d%d",&p,&q);
	if(n==p){
		printf("Test case 1: Matrix multiplication can be done\n");
		printf("Enter the element of A: ");
		int x = getMat(m,n,a);
		if(x) goto end;
		printf("Enter the element of B: ");
		x += getMat(p,q,b);
		if(x) goto end;
		//multiplication
		for(int i=0; i<m; i++){
			for(int j=0; j<q; j++){
				c[i][j]=0;
				for(int k=0; k<n; k++){
					c[i][j] += a[i][k]*b[k][j];
				}
			}
		}
		//print the result
		for(i=0; i<m; i++){
			for (int j=0; j<q; j++){
				printf("%d ",c[i][j]);
			}
			printf("\n");
		}
	}else{
		printf("Test case 2: Not equal n and p\n");
	}
	end: getch();
	return 0;
}
