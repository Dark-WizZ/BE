#include<conio.h>
#include<stdio.h>
void main()
{
  int a,b,c,result;
  printf(" Enter the values of a, b and c : = ");
  scanf("%d %d %d", &a,&b,&c);
  if(((a+b)>c)&&((b+c)>a)&&((c+a)>b))
  {
    if((a==b)&&(b==c))
      printf("\n It is an Equilateral Triangle");
    else if((a==b)||(b==c)||(c==a))
      printf("\n It is an Isosceles Triangle");
    else
      printf("\n It is a Scalene Triangle");
  }
  else
  printf("\n Not a Triangle");
  getch();
}
