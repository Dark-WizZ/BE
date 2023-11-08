#include <graphics.h>
#include <stdlib.h>

void draw()
{
		char ch;
		int x1, x2, y1, y2, dx, dy;
		int i;
		for (i = 0; i < 10000; i++){
				ch = random(3);
				if (ch == 0){
						dx=320; dy=0;
				}
				else if (ch == 1){
						dx=0; dy=480;
				}
				else{
						dx=640; dy=480;
				}
				x1=(x2+dx)/2;
				y1=(y2+dy)/2;
				putpixel(x1, y1, YELLOW);
				x2 = x1;
				y2 = y1;
		}
}
void main()
{
		int gd = DETECT, gm;
		initgraph(&gd, &gm, "..//BGI");
		draw();
		getch();
}