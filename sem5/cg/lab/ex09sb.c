#include <GL/glut.h>

float angle = 0;

void display(){
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();
	glTranslatef(0,0,-5);
	glRotatef(angle,1,1,1);
	
	glBegin(GL_QUADS);
	
   glColor3f(1, 0, 1);
    glVertex3f(1, 1, 1);
    glVertex3f(1, 1, -1);
    glVertex3f(1, -1, -1);
    glVertex3f(1, -1, 1);

    glColor3f(0, 1, 1);
    glVertex3f(-1, 1, 1);
    glVertex3f(-1, 1, -1);
    glVertex3f(-1, -1, -1);
    glVertex3f(-1, -1, 1);
    
    glColor3f(1, 0, 0);
    glVertex3f(1, 1, 1);
    glVertex3f(1, 1, -1);
    glVertex3f(-1, 1, -1);
    glVertex3f(-1, 1, 1);

    glColor3f(0, 1, 0);
    glVertex3f(1, -1, 1);
    glVertex3f(1, -1, -1);
    glVertex3f(-1, -1, -1);
    glVertex3f(-1, -1, 1);

    glColor3f(0, 0, 1);
    glVertex3f(1, 1, 1);
    glVertex3f(1, -1, 1);
    glVertex3f(-1, -1, 1);
    glVertex3f(-1, 1, 1);

    glColor3f(1, 1, 0);
    glVertex3f(1, 1, -1);
    glVertex3f(1, -1, -1);
    glVertex3f(-1, -1, -1);
    glVertex3f(-1, 1, -1);

	
	glEnd();
	
	angle += 0.1;
	
	glutSwapBuffers();
}
void reshape(int w, int h){
	glViewport(0, 0 , w, h);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluPerspective(45, (float)w/h,1,100);
	glMatrixMode(GL_MODELVIEW);
}
void idle(){
	glutPostRedisplay();
}

main(int argc, char** argv){
	glutInit(&argc,argv);
	glutCreateWindow("rotation");
	glEnable(GL_DEPTH_TEST);
	glutDisplayFunc(display);
	glutReshapeFunc(reshape);
	glutIdleFunc(idle);
	glutMainLoop();
}
