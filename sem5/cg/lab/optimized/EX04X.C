#include <graphics.h>
#include <math.h>

float xs[4],ys[4];
float theta, dxs[4],dys[4], dy, dx, xp, yp, deg, piv[2];
int gm, gd=DETECT, ch, i, flag;

void rectany(float xs[], float ys[]){
	line(xs[0],ys[0],xs[1],ys[1]);
	line(xs[1],ys[1],xs[2],ys[2]);
	line(xs[2],ys[2],xs[3],ys[3]);
	line(xs[3],ys[3],xs[0],ys[0]);
}
void translate(float dx, float dy){
	rectangle(xs[0]+dx,ys[0]+dy,xs[2]+dx,ys[2]+dy);
}
void rotate(float deg, float xs[], float ys[],float piv[]){
	theta = deg*(3.14/180);
	for(i=0; i<4; i++){
		dxs[i] = piv[0] + ((xs[i] - piv[0]) * cos(theta) - (ys[i] - piv[1]) * sin(theta));
		dys[i] = piv[1] + ((xs[i] - piv[0]) * sin(theta) + (ys[i] - piv[1]) * cos(theta));
	}
	rectany(dxs,dys);
}
void scale(float dx, float dy){
	rectangle(xs[0]*dx,ys[0]*dy,xs[2]*dx,ys[2]*dy);
}
void reflect(int flag, float pv[]){
	float tempx[4], tempy[4];
	deg=180;
	for(i=0;i<4;i++){
		tempx[i]=xs[i]; tempy[i]=ys[i];
		if(flag==1){
			tempy[i]=-ys[i];deg=90;
		}else if(flag==2){
			tempx[i]=-xs[i];deg=270;
		}else if(flag==3){
			tempx[i]=-xs[i];tempy[i]=-ys[i];
		}
	}
	rotate(deg,tempx,tempy,pv);
}
void shear(int ch, float fac){
	for(i=0;i<4;i++){
		dxs[i] = xs[i];dys[i]=ys[i];
	}
	if(ch==1){
		dxs[0]=xs[0]+fac;
		dxs[1]=xs[1]+fac;
	}else if(ch==2){
		dys[1]=ys[1]+fac;
		dys[2]=ys[2]+fac;
	}
	rectany(dxs,dys);
}
void main(){
	initgraph(&gd,&gm,"..\\bgi");
	printf("Enter upper left of the rectange: ");
	scanf("%f%f",&xs[0],&ys[0]);
	printf("Enter lower right of the rectangle: ");
	scanf("%f%f",&xs[2],&ys[2]);
	xs[1]=xs[2];
	ys[1]=ys[0];
	xs[3]=xs[0];
	ys[3]=ys[2];
	rectany(xs,ys);
	while (1)  {
		printf("******2DTransformations*******\n");
		printf("1.Translation\n 2.Rotation\n 3.Scaling\n 4.Reflection\n 5.Shearing\n 6.Exit\n Enter your choice:\n");
		scanf("%d",&ch);
		initgraph(&gd,&gm,"..\\bgi");
		rectangle(xs[0],ys[0],xs[2],ys[2]);
		switch(ch){
			case 1:
				printf("*******Translation*******\n\n");
				printf("Enter the value of shift vector:\n");
				scanf("%f%f", &dx, &dy);
				translate(dx, dy);
				break;
			case 2:
				printf("*********Rotation********\n\n");
				printf("Enter the values of fixed point and degree of rotation;\n");
				scanf("%f%f%f",&piv[0],&piv[1],&deg);
				rotate(deg, xs, ys, piv);
				break;
			case 3:
				printf("********Scaling*******\n\n");
				printf("Enter the value of scaling factor:\n");
				scanf("%f%f",&dx,&dy);
				scale(dx, dy);
				break;
			case 4:
				printf("*******Reflection*********\n");
				printf("1.About x-axis\n2.About y-axis\n3.About both axis\nEnter your choice:\n");
				scanf("%d",&ch);
				printf("Enter the values for fixed point: ");
				scanf("%f%f",&piv[0],&piv[1]);
				reflect(ch,piv);
				break;
			case 5:
				printf("*******Shearing******\n\n");
				printf("1.x-direction shear\n2.y-direction shear\nEnter your choice:\n");
				scanf("%d",&ch);
				printf("\nEnter the shearing factor: ");
				scanf("%f",&dx);
				shear(ch,dx);
				break;
			case 6:
				exit(0);
		}
	}getch();
	getch();
}