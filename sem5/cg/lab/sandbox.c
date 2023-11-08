#include <stdio.h>
#include <graphics.h>

void drawEllipse(int x_center, int y_center, int rx, int ry) {
    int x = 0, y = ry;
    int p1 = ry * ry - rx * rx * ry + (rx * rx) / 4;
    
    while (2 * ry * ry * x <= 2 * rx * rx * y) {
        putpixel(x_center + x, y_center + y, WHITE);
        putpixel(x_center - x, y_center + y, WHITE);
        putpixel(x_center + x, y_center - y, WHITE);
        putpixel(x_center - x, y_center - y, WHITE);
        
        if (p1 < 0) {
            x++;
            p1 += 2 * ry * ry * x + ry * ry;
        } else {
            x++;
            y--;
            p1 += 2 * ry * ry * x - 2 * rx * rx * y + ry * ry;
        }
    }
}

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "C:\\Turboc3\\BGI");

    int x_center = 200; // X-coordinate of the center
    int y_center = 200; // Y-coordinate of the center
    int rx = 100;       // Major axis radius
    int ry = 50;        // Minor axis radius

    drawEllipse(x_center, y_center, rx, ry);

    getch();
    closegraph();
    return 0;
}