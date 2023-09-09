#include <graphics.h>
#include <math.h>
struct points{
	float x[8], y[8], z[8];
};
struct points p1, p2, dp1, dp2;
float x, y, z, d, dx, dy, dz;
int gd=DETECT, gm, i, ch;
void init(){
	initgraph(&gd, &gm, "..//bgi");
}
void recany(float x0, float y0, float x1, float y1,
						float x2, float y2, float x3, float y3){
	line(x0,y0,x1,y1);
	line(x1,y1,x2,y2);
	line(x2,y2,x3,y3);
	line(x3,y3,x0,y0);
}
void create(){
	for(i=0; i<8; i++){
		p1.x[i]=x;
		p1.y[i]=y;
		p1.z[i]=z;
	}
	for(i=4; i<8; i++) p1.z[i]-=d;
	p1.x[1]+=d; p1.x[2]+=d;
	p1.y[2]+=d; p1.y[3]+=d;
	p1.x[5]+=d; p1.x[6]+=d;
	p1.y[6]+=d; p1.y[7]+=d;
	for(i=0; i<8; i++){
		p2.x[i]=p1.x[i]+p1.z[i]/2;
		p2.y[i]=p1.y[i]+p1.z[i]/2;
	}
}
void drawcube(struct points p){
	recany(p.x[0],p.y[0],p.x[1],p.y[1],p.x[2],p.y[2],p.x[3],p.y[3]);
	recany(p.x[4],p.y[4],p.x[5],p.y[5],p.x[6],p.y[6],p.x[7],p.y[7]);
	line(p.x[0],p.y[0],p.x[4],p.y[4]);
	line(p.x[1],p.y[1],p.x[5],p.y[5]);
	line(p.x[2],p.y[2],p.x[6],p.y[6]);
	line(p.x[3],p.y[3],p.x[7],p.y[7]);
}
void translate(){
	for(i=0;i<8;i++){
		dp1.x[i]=p1.x[i]+dx;
		dp1.y[i]=p1.y[i]+dy;
		dp1.z[i]=p1.z[i]+dz;
		dp2.x[i]=dp1.x[i]+dp1.z[i]/2;
		dp2.y[i]=dp1.y[i]+dp1.z[i]/2;
	}
}
void scale(){
	for(i=0;i<8;i++){
		dp1.x[i]=p1.x[i]*dx;
		dp1.y[i]=p1.y[i]*dy;
		dp1.z[i]=p1.z[i]*dz;
		dp2.x[i]=dp1.x[i]+dp1.z[i]/2;
		dp2.y[i]=dp1.y[i]+dp1.z[i]/2;
	}
}
void rotate(int flag, float theta){
	for(i=0;i<8;i++){
		dp1.x[i]=p1.x[i];
		dp1.y[i]=p1.y[i];
		dp1.z[i]=p1.z[i];
		if(flag==1){
			dp1.y[i]=(p1.y[i]-y)*cos(theta)+(p1.z[i]-z)*sin(theta)+y;
			dp1.z[i]=(p1.y[i]-y)*sin(theta)+(p1.z[i]-z)*cos(theta)+z;
		}else if(flag==2){
			dp1.x[i]=(p1.x[i]-x)*cos(theta)+(p1.z[i]-z)*sin(theta)+x;
			dp1.z[i]=(p1.x[i]-x)*sin(theta)+(p1.z[i]-z)*cos(theta)+z;
		}else if(flag==3){
			dp1.x[i]=(p1.x[i]-x)*cos(theta)+(p1.y[i]-y)*sin(theta)+x;
			dp1.y[i]=(p1.x[i]-x)*sin(theta)+(p1.y[i]-y)*cos(theta)+y;
		}
		dp2.x[i]=dp1.x[i]+dp1.z[i]/2;
		dp2.y[i]=dp1.y[i]+dp1.z[i]/2;
	}
}
void main(){
	clrscr();
	init();
	printf("Enter x, y, z for cube: ");
	scanf("%f%f%f",&x,&y,&z);
	printf("Enter size of sides: ");
	scanf("%f",&d);
	create();
	drawcube(p2);
	getch();
	while(1){
		clrscr();
		init();
		printf("3D transformation: \n");
		printf("1.Translate\n2.Scale\n3.Rotate\n0.Exit\n\n");
		printf("Enter your choice: ");
		scanf("%d",&ch);
		clrscr();
		init();
		switch(ch){
			case 1:
				printf("Enter translation factor(x,y,z): ");
				scanf("%f%f%f",&dx,&dy,&dz);
				drawcube(p2);
				translate();
				drawcube(dp2);
				break;
			case 2:
				printf("Enter the scaling factor(x,y,z): ");
				scanf("%f%f%f",&dx,&dy,&dz);
				drawcube(p2);
				scale();
				drawcube(dp2);
				break;
			case 3:
				printf("Rotation axis: \n");
				printf("1. X-Axis\n2. Y-Axis \n3. Z-Axis \n");
				printf("Enter your choice: ");
				scanf("%d",&ch);
				printf("Enter rotaion angle: ");
				scanf("%f",&d);
				drawcube(p2);
				rotate(ch,d*180/3.14);
				drawcube(dp2);
				break;
			case 0:
				exit(0);
		}
		getch();

	}
	getch();
}
