#include <graphics.h>
#include <math.h>

void main(){
	float x1,x2,x3,y1,y2,y3;
	float w1=5, w2=5, w3=635, w4=465;
	float v1=425, v2=75, v3=550, v4=250;
	float dx,dy;
	int gd=DETECT, gm;
	clrscr();
	initgraph(&gd,&gm,"..\\bgi");
	printf("Enter three coords: \n");
	scanf("%f%f%f%f%f%f",&x1,&y1,&x2,&y2,&x3,&y3);
	rectangle(w1,w2,w3,w4);
	line(x1,y1,x2,y2);
	line(x2,y2,x3,y3);
	dx=(v3-v1)/(w3-w1);
	dy=(v4-v2)/(w4-w2);
	x1= v1 + ((x1-w1)*dx);
	x2= v1 + ((x2-w1)*dx);
	x3= v1 + ((x3-w1)*dx);
	y1= v2 + ((y1-w2)*dy);
	y2= v2 + ((y2-w2)*dy);
	y3= v2 + ((y3-w2)*dy);
	rectangle(v1,v2,v3,v4);
	line(x1,y1,x2,y2);
	line(x2,y2,x3,y3);
	getch();
}