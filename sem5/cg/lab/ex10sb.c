#include <GL/glut.h>

void init(){
	glMatrixMode(GL_PROJECTION);
	gluOrtho2D(0, 800, 0, 800);
}
void display(){
	int i, j, c=0;
	glClear( GL_COLOR_BUFFER_BIT);	
	
	
	
	for(i=0; i<=700; i+=100){
		for(j=0; j<=700; j +=100){
			glBegin(GL_POLYGON);
			if(c==0){
				glColor3f(0,0,0); c=1;	
			}else{
				glColor3f(1,1,1); c=0;
			} 
			glVertex2f(i, j);
			glVertex2f(i+100, j);
			glVertex2f(i+100, j+100);
			glVertex2f(i, j+100);
			glEnd();
		}
	}
	glFlush();
}
main(int argc, char** argv){
	glutInit(&argc, argv);
	glutCreateWindow("Chess board");
	init();
	glutDisplayFunc(display);
	glutMainLoop();
}
