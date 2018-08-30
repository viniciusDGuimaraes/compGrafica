from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

n = 50

vertices = [
    [ 1,-1,-1],
    [ 1, 1,-1],
    [-1, 1,-1],
    [-1,-1,-1],
    [ 1,-1, 1],
    [ 1, 1, 1],
    [-1,-1, 1],
    [-1, 1, 1],
    ]

linhas = [
    [0,1],
    [0,3],
    [0,4],
    [2,1],
    [2,3],
    [2,7],
    [6,3],
    [6,4],
    [6,7],
    [5,1],
    [5,4],
    [5,7],
    ]

faces = [
    [0,1,2,3],
    [3,2,7,6],
    [6,7,5,4],
    [4,5,1,0],
    [1,5,7,2],
    [4,0,3,6]
    ]

cores = [ [1,0,0],[1,1,0],[0,1,0],[0,1,1],[0,0,1],[1,0,1],[0.5,1,1],[1,0,0.5], [1,0,0.2], [0.2,1,0.5]]

def Piramede():
    glBegin(GL_POLYGON)
    
    x = 1
    z = 0

    for i in range(0, n):
        glColor3fv([1, 0.5 ,0.5])
        glVertex3fv([(math.cos(2 * math.pi * i / n)), -1, (math.sin(2 * math.pi * i / n))])
        x += 2 * math.pi / n
        z += 2 * math.pi / n

    glEnd()

    glBegin(GL_TRIANGLE_FAN)

    glColor3fv(cores[0])
    glVertex3fv([0, 1, 0])

    x = 1
    z = 0

    for i in range(0,n + 1):
        glColor3fv(cores[i % len(cores)])
        glVertex3fv([(math.cos(2 * math.pi * i / n)), -1, (math.sin(2 * math.pi * i / n))])
        x += 2 * math.pi / n
        z += 2 * math.pi / n

    glEnd()

def abacaxi():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    Piramede()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Piramede")
glutDisplayFunc(abacaxi)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-8)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()


