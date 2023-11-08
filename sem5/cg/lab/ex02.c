#include <stdio.h>
#include <conio.h>
#include <graphics.h>
#include <math.h>
#include <dos.h>
void main()
{
  long int p, p;
  int i, gd = DETECT, gm, x, y;
  long int rx, ry, rxsq, rysq, tworxsq, tworysq, dx, dy;
  printf("Enter the x Radius of the ellipse");
  scanf("%ld", &rx);
  printf("Enter the y Radius of the ellipse");
  scanf("%ld", &ry);
  initgraph(&gd, &gm, " ");
  rxsq = rx * rx;
  rysq = ry * ry;
  tworxsq = 2 * rxsq;
  tworysq = 2 * rysq;
  x = 0;
  y = ry;
  p = rysq - (rxsq * ry) + (0.25 * rxsq);
  dx = tworysq * x;
  dy = tworxsq * y;
  while (dx < dy)
  {
    putpixel(200 + x, 200 + y, 15);
    putpixel(200 - x, 200 - y, 15);
    putpixel(200 + x, 200 - y, 15);
    putpixel(200 - x, 200 + y, 15);
    x++;
    dx += tworysq;
    p += dx + rysq;
    if (p < 0)
    {
    }
    else
    {
      y--;
      dy -= tworxsq;
      p -= - dy;
    }
    delay(50);
  }
  p = rysq * (x + 0.5) * (x + 0.5) + rxsq * (y - 1) * (y - 1) - rxsq * rysq;
  while (y > 0)
  {
    putpixel(200 + x, 200 + y, 15);
    putpixel(200 - x, 200 - y, 15);
    putpixel(200 + x, 200 - y, 15);
    putpixel(200 - x, 200 + y, 15);
    y--;
    dy -= tworxsq;
    if (p > 0)
    {
      p -= dy + rxsq;
    }
    else
    {
      x++;
      dx += tworysq;
      p += dx - dy + rxsq;
    }
    delay(50);
  }
  getch();
  closegraph();
}