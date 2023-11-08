#include<stdio.h>
#include<graphics.h>
void drawCircle(int r){
	int p=1-r, i;
	int x=0, y=r;
	int xpiv=320;
	int ypiv=240;
	while(x<y){
		putpixel(xpiv+x,ypiv+y,7);
		putpixel(xpiv-x,ypiv+y,7);
		putpixel(xpiv+x,ypiv-y,7);
		putpixel(xpiv-x,ypiv-y,7);
		putpixel(xpiv+y,ypiv+x,7);
		putpixel(xpiv-y,ypiv+x,7);
		putpixel(xpiv+y,ypiv-x,7);
		putpixel(xpiv-y,ypiv-x,7);
		p += (2*x)+3;
		x++;
		if(p >= 0){
			p -= (2*y)+2;
			y--;
		}
	}
}
void main(){
	int gd=DETECT,gm=0,xa,ya,r,p,k,x,y;
	initgraph(&gd,&gm,"..\\BGI");
	printf("Enter the radius");
	scanf("%d",&r);
	drawCircle(r);
	getch();
}
