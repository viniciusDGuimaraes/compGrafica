from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import cos, sin, pi, tan

cores = [ [1,0,0],[1,1,0],[0,1,0],[0,1,1],[0,0,1],[1,0,1],[0.5,1,1],[1,0,0.5], [1,0,0.2], [0.2,1,0.5]]

def MarxistFunction(theta, phi, r):
    return [r*cos(phi)*cos(theta), r*sin(phi), r*cos(phi)*sin(theta)]

def Revolucion():
    glBegin(GL_QUADS)

    i = 0
    division = 20

    phi = -pi/2
    delta = pi/division

    while phi <= pi/2:
        theta = 0
        while theta <= 2*pi:
#            glColor3fv(cores[i % len(cores)])
#            glColor3fv([cos(theta), sin(phi), 0.3])
            glVertex3fv(MarxistFunction(theta, phi, 1))
            glVertex3fv(MarxistFunction(theta + delta, phi, 1))
            glVertex3fv(MarxistFunction(theta + delta, phi + delta, 1))
            glVertex3fv(MarxistFunction(theta, phi + delta, 1))
            theta += delta
            i += 1
        phi += delta

    glEnd()

def abacaxi():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    Revolucion()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Viva la Revolucion")
glutDisplayFunc(abacaxi)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-5)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()

