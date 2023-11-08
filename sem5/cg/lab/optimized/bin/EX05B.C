#include <stdio.h>
#include <conio.h>
#include <graphics.h>
#include <math.h>
main(){
	float sx, sy;
	float w1, w2, w3, w4, x1, x2, x3, x4, y1, y2, y3, y4, v1, v2, v3, v4;
	int gd = DETECT, gm;
	initgraph(&gd, &gm, "..//bgi");
	printf("Enter the Co-ordinates x1,y1,x2,y2,x3,y3\n");
	scanf("%f%f%f%f%f%f", &x1, &y1, &x2, &y2, &x3, &y3);
	cleardevice();
	w1 = 5;
	w2 = 5;
	w3 = 635;
	w4 = 465;
	rectangle(w1, w2, w3, w4);
	line(x1, y1, x2, y2);
	line(x2, y2, x3, y3);
	getch();
	v1 = 425;
	v2 = 75;
	v3 = 550;
	v4 = 250;
	sx = (v3 - v1) / (w3 - w1);
	sy = (v4 - v2) / (w4 - w2);
	rectangle(v1, v2, v3, v4);
	x1 = v1 + ((x1 - w1) * sx);
	x2 = v1 + ((x2 - w1) * sx);
	x3 = v1 + ((x3 - w1) * sx);
	y1 = v2 + ((y1 - w2) * sy);
	y2 = v2 + ((y2 - w2) * sy);
	y3 = v2 + ((y3 - w2) * sy);

	printf("%f, %f, %f, %f, %f, %f \ndx=%f,dy=%f",x1,y1,x2,y2,x3,y2,sx,sy);
	line(x1, y1, x2, y2);
	line(x2, y2, x3, y3);
	getch();
	return 0;
}