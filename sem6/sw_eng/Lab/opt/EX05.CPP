#include <stdio.h>
#include <conio.h>

void main(){
	int a, b, t;
	clrscr();
	printf("Enter the first number: ");
	scanf("%d",&a);
	printf("Enter the second number: ");
	scanf("%d",&b);
	if(a<b){
		t=a;
		a=b;
		b=t;
	}
	printf("%d %d",a,b);
	getch();
}