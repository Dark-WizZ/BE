#include <stdio.h>
#include <conio.h>
int count=0;
void nat_of_roots(int a, int b, int c){
	count++;
	printf("\n%d\t\t%d\t%d\t%d\t",count,a,b,c);
	if(a==0){
		printf("not a quad eq");
		return;
	}
	int d = (b*b) - (4*a*c);
	if(d>0)
		printf("Real roots");
	else if(d==0)
		printf("equal roots");
	else
		printf("imaginary roots");
}
void main(){
	clrscr();
	int t[4]={0,1,99,100};
	printf("\nCase\t\ta\tb\tc\tresult");
	nat_of_roots(50,50,50);
	for(int i=0; i<4; i++) nat_of_roots(t[i], 50, 50);
	for(i=0; i<4; i++) nat_of_roots(50, t[i], 50);
	for(i=0; i<4; i++) nat_of_roots(50, 50, t[i]);
	getch();
}