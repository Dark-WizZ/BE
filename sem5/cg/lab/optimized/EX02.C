#include <stdio.h>
#include <graphics.h>

long int sq(int num){
	return num*num;
}
void drawEll(int rx, int ry){
	long int dy, dx;
	int x=0, y=ry, xp=320, yp=240;
	long int rxsq=sq(rx), rysq=sq(ry);
	long int p = rysq - (rxsq*y);
	dx = 2*rysq*x;
	dy = 2*rxsq*y;
	while(dx<dy){
		putpixel(xp+x,yp+y,RED);
		putpixel(xp+x,yp-y,RED);
		putpixel(xp-x,yp+y,RED);
		putpixel(xp-x,yp-y,RED);
		x++;
		dx += 2*rysq;
		p += dx + rysq;
		if(p>=0){
			y--;
			dy -= 2*rxsq;
			p -= dy;
		}
	}
	p = rysq*sq(x) + rxsq*sq(y) - rxsq*rysq;
	while(y>0){
		putpixel(xp+x,yp+y,7);
		putpixel(xp+x,yp-y,7);
		putpixel(xp-x,yp+y,7);
		putpixel(xp-x,yp-y,7);
		y--;
		dy -= 2*rxsq;
		p -= dy + rxsq;
		if(p<0){
			x++;
			dx += 2*rysq;
			p += dx;
		}
	}
}
void main(){
	long int p;
	int i, gd = DETECT, gm;
	int rx, ry;
	clrscr();
	printf("Enter the x Radius of the ellipse: ");
	scanf("%d", &rx);
	printf("Enter the y Radius of the ellipse: ");
	scanf("%d", &ry);
	initgraph(&gd, &gm, "..\\bgi");
	drawEll(rx, ry);
	getch();
	closegraph();
}