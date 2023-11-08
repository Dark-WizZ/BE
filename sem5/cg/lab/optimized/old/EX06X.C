#include <graphics.h>

int gd=DETECT, gm, i, n, j, k;
int vs[20];
float xmin, xmax, ymin, ymax;
int code[4], c1[4], c2[4], flag;
float x1, y1, x2, y2, m;

void codegen(float x, float y, int c[]){
	if(x<xmin) c[3]=1;
	if(x>xmax) c[2]=1;
	if(y<ymin) c[1]=1;
	if(y>ymax) c[0]=1;
}

void clip(int c[], float *x, float *y, float x1, float y1){
	if(c[0]==1) {
		*x = ((ymax-y1)/m) + x1; *y = ymax;
		if(m==0) *x = x1;
	}
	if(c[1]==1){
		*x = ((ymin-y1)/m)+x1; *y = ymin;
		if(m==0) *x = x1;
	}
	if(c[2]==1){
		*y = m*(xmax-x1)+y1; *x = xmax;
		if(m==0) *y = y1;
	}
	if(c[3]==1){
		*y = m*(xmin-x1)+y1; *x = xmin;
		if(m==0) *y = y1;
	}
}
void lineclip(){
	 for(j=0;j<n;j++){
		flag=0; k=j*2;
		x1=vs[k]; y1=vs[k+1];
		x2=vs[k+2]; y2=vs[k+3];
		for(i=0; i<4; i++){
			c1[i]=0; c2[i]=0;code[i]=0;
		}
		if(x2-x1==0) m=0;
		else m=(y2-y1)/(x2-x1);
		codegen(x1,y1,c1);
		codegen(x2,y2,c2);
		for(i=0; i<4; i++){
			code[i] = c1[i] && c2[i];
			if(code[i]==1) flag=1;
		}
		if(flag==1){
			x1=x2=y1=y2=0;
		}else{
			for(i=0; i<4; i++)
				if(c1[i]==1||c2[i]==1) flag=1;
				if(flag==1){
					clip(c1,&x1,&y1,x2,y2);
					clip(c2,&x2,&y2,x1,y1);
				}
			}
		rectangle(xmin,ymin,xmax,ymax);
		line(x1,y1,x2,y2);
	}
}

void main(){
	clrscr();
	initgraph(&gd,&gm,"..\\bgi");
	printf("Enter the no. vertices:");
	scanf("%d",&n);
	for(i=0; i<n; i++){
		printf("Enter co-ords of vertex %d: ",i+1);
		scanf("%d%d",&vs[i*2],&vs[(i*2)+1]);
	}
	vs[i*2]=vs[0];
	vs[(i*2)+1]=vs[1];
	printf("Enter co-ords for window: ");
	scanf("%f%f%f%f",&xmin,&ymin,&xmax,&ymax);
	rectangle(xmin,ymin,xmax,ymax);
	drawpoly(n+1,vs);
	getch();
	clrscr();
	cleardevice();
	lineclip();
	getch();
}