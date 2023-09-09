#include <graphics.h>

int gm, gd=DETECT;
float x1, y1, x2, y2, xmin, xmax, ymin, ymax, m;
int c1[4]={0,0,0,0},c2[4]={0,0,0,0}, code[4];
int i, flag=0;

void codegen(float x, float y, int c[]){
	if(x<xmin) c[3]=1;
	if(x>xmax) c[2]=1;
	if(y<ymin) c[1]=1;
	if(y>ymax) c[0]=1;
}

void clip(int c[], float *x, float *y, float x1, float y1){
	printf("x1->%f, y1->%f, x2->%f, y2->%f\n",*x,*y,x1,y1);
	if(c[0]==1) {
		*x = ((ymax-y1)/m)+x1; *y = ymax;
		if (m==0) *x=x1;
	}
	if(c[1]==1){
		*x = ((ymin-y1)/m)+x1; *y = ymin;
		if(m==0) *x=x1;
		printf("m=%f, x=%f\n",m,*x);getch();
	}
	if(c[2]==1){
		*y = m*(xmax-x1)+y1; *x = xmax;
		if(m==0) *y=y1;
	}
	if(c[3]==1){
		*y = m*(xmin-x1)+y1; *x = xmin;
		if(m==0) *y=y1;
	}
}

void main(){
	clrscr();
	initgraph(&gd, &gm, "..\\bgi");
	printf("Enter 1st coords of line: ");
	scanf("%f%f",&x1,&y1);
	printf("Enter 2nd coords of line: ");
	scanf("%f%f",&x2,&y2);
	printf("Enter coords of window: ");
	scanf("%f%f%f%f",&xmin,&ymin,&xmax,&ymax);
	rectangle(xmin,ymin,xmax,ymax);
	line(x1,y1,x2,y2);
	getch();
	if (x2-x1==0)m=0;
	else m=(y2-y1)/(x2-x1);
	codegen(x1,y1,c1);
	codegen(x2,y2,c2);
	for(i=0; i<4; i++){
	 code[i] = c1[i] && c2[i];
	 if(code[i]==1) flag=1;
	}
	if(flag==1){
		printf("\nThe line is fully outside");
		x1=x2=y1=y2=0;
	}else{
		for(i=0; i<4; i++)
			if(c1[i]==1||c2[i]==1) flag=1;
		if(flag==0){
			printf("\nThe line is completely inside");
		}else{
			printf("\nThe line is partially inside");
			clip(c1,&x1,&y1,x2,y2);
			clip(c2,&x2,&y2,x1,y1);
		}
	}
	getch();
	clrscr();
	cleardevice();
	printf("\nAfter clipping");
	rectangle(xmin,ymin,xmax,ymax);
	line(x1,y1,x2,y2);
	getch();
}