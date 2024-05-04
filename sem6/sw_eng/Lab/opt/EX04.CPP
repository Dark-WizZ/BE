#include <stdio.h>
#include <conio.h>

void main(){
	clrscr();
	int a,b,c;
	do{
	printf("\nEnter the value of A, B, C: ");
	scanf("%d %d %d",&a,&b,&c);
	if(((a+b)>c) && ((b+c)>a) && ((c+a)>b)){
		if((a==b) && (b==c))
			printf("Equilateral triangle");
		else if((a==b) || (b==c) || (c==a))
			printf("Isolene triangle");
		else
			printf("Scalene triangle");
	}else{
		printf("Not an triagle!!!");
	}}while(a!=0 && b!=0 && c!=0);
	getch();
}