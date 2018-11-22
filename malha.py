from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import cos, sin, pi, tan

def Revolucion():
    glBegin(GL_QUADS)

    x     = -1.5
    delta = 0.1
    tamx  = 1.6
    tamy  = 1.5

    while x < tamx:
        y = -1.5
        while y < tamy:
            glVertex3fv([x        , 0.0, y        ])
            glVertex3fv([x        , 0.0, y + delta])
            glVertex3fv([x + delta, 0.0, y + delta])
            glVertex3fv([x + delta, 0.0, y        ])

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
