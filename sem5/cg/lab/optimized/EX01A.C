#include <stdio.h>
#include <graphics.h>
void drawline(int x0, int y0, int x1, int y1){
	int dx, dy, p, x=x0, y=y0;
	dx=x1-x0;
	dy=y1-y0;
	p=2*dy-dx;
	while((x<=x1) && (y<=y1)){
		putpixel(x,y,7);
		x++;
		p+=2*dy;
		if(p>=0){
			y++;
			p -= 2*dx;
		}
	}
}
int main(){
	int gdriver=DETECT, gmode, error, x0, y0, x1, y1;
	initgraph(&gdriver, &gmode, "c:\\turboc3\\bgi");
	printf("Enter first co-ordinates point: ");
	scanf("%d%d", &x0, &y0);
	printf("Enter second co-ordinates point: ");
	scanf("%d%d", &x1, &y1);
	drawline(x0, y0, x1, y1);
	getch();
	return 0;
}