from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import cos, sin, pi, tan


def MarxistFunction(theta, phi, r):
    c = 2
    return [(c + r * sin(phi)) * sin(theta), r * cos(phi), (c + r*sin(phi)) * cos(theta)]

def Revolucion():
    glBegin(GL_QUADS)

    division = 20
    r = 1

    phi = 0
    delta = pi/division

    while phi < 2*pi:
        theta = 0
        while theta < 2*pi:
            glColor3fv([cos(theta), cos(phi), 0.3])
            glVertex3fv(MarxistFunction(theta, phi, r))
            glVertex3fv(MarxistFunction(theta + delta, phi, 1))
            glVertex3fv(MarxistFunction(theta + delta, phi + delta, 1))
            glVertex3fv(MarxistFunction(theta, phi + delta, 1))
            theta += delta
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
gluPerspective(75,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-5)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()

