from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import cos, sin, pi, tan

cores = [ [1,0,0],[1,1,0],[0,1,0],[0,1,1],[0,0,1],[1,0,1],[0.5,1,1],[1,0,0.5], [1,0,0.2], [0.2,1,0.5]]

def FindZ(x, y):
    return [x, (-x**2+y**2), y]

def Revolucion():
    glBegin(GL_QUADS)

    x = -1.5
    delta = 0.1
    tam = 1.5

    while x < tam:
        y = -1.5
        while y < tam:
            glColor3fv([cos(x), sin(y), 0.3])
            glVertex3fv(FindZ(x, y))
            glVertex3fv(FindZ(x + delta, y))
            glVertex3fv(FindZ(x + delta, y + delta))
            glVertex3fv(FindZ(x, y + delta))
            y += delta
        x += delta

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
glutCreateWindow("Malha")
glutDisplayFunc(abacaxi)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(90,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-5)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()
