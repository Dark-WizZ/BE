#include <stdio.h>
#include<conio.h>
1.
void main()
2.
{
3.
int a,b, t;
4.
clrscr();
5.
printf(“Enter the first number”);
6.
scanf(“%d”, &b);
7.
printf(“Enter the second number”);
8.
scanf(“%d”, &b);
if (a<b) {
t=a;
a=b;
b=t;
}
printf(“%d%d”, a,b);
getch();
}
