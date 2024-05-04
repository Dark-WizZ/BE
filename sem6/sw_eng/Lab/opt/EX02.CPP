#include <stdio.h>
#include <conio.h>

int binser(int a[], int l, int h, int k){
	int m;
	while(l<=h){
		m = (l+h)/2;
		if(a[m]==k)
			return m+1;
		else if(k<a[m])
			h=m-1;
		else
			l=m+1;
	}
	return -1;
}
void main(){
	clrscr();
	int k, a[10], n;
	printf("Enter size: ");
	scanf("%d",&n);
	printf("Enter in asc order: ");
	for (int i=0; i<n; i++) scanf("%d",&a[i]);
	do{
		printf("\nKey: ");
		scanf("%d",&k);
		int c = binser(a,0,n-1,k);
		if(c>0)
			printf("\nfound in pos = %d",c);
		else
			printf("not found");
	}while(k);
}