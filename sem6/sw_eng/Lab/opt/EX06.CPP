#include <stdio.h>
#include <conio.h>

void main(){
clrscr();
printf("While loop\n");
int i=0;
printf("Before loop i = %d\n",i);
while(i<5){
	printf("i = %d\n",i++);
}
printf("After loop i = %d\n",i);
getch();
printf("\nDo-While loop\n");
int month = 0;
do{
	printf("Enter month: ");
	scanf("%d",&month);
}while(month<1 || month>12);
printf("Program finished.");
getch();
}