import math
import random
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

'''
vertices = (
    ( 1,-1,-1),
    ( 1, 1,-1),
    (-1, 1,-1),
    (-1,-1,-1),
    ( 1,-1, 1),
    ( 1, 1, 1),
    (-1,-1, 1),
    (-1, 1, 1),
    )
linhas = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7),
    )
faces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )
'''

vertices = (
    ( 1,-1,-1),
    ( 1, 1,-1),
    (-1, 1,-1),
    (-1,-1,-1),
    ( 1,-1, 1),
    ( 1, 1, 1),
    (-1,-1, 1),
    (-1, 1, 1),
    )

linhas = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7),
    )

faces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )

cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )

contador = 0.0

def polygonRevolucao():
	global contador
	r = 1.0
	c = (math.sin(contador)+1.1)*1.5

	'''
	c = ((math.sin(contador)/contador)+(math.sin(contador*3)/contador*3)+(math.sin(contador*5)/contador*5)+(math.sin(contador*7)/contador*7)) fourier
	
	def t(u, v):
		return((c + r * math.cos(u)) * math.cos(v), r * math.sin(u), (c + r * math.cos(u)) * math.sin(v))
	'''

	
	def s(u, v):
		return((c + r * math.sin(v)) * math.sin(u), r * math.cos(v), (c + r * math.sin(v)) * math.cos(u))
	
	delta = 0.0
	phi = 0.0
	aux = 0.1

	while delta <= (math.pi * 2):
		glBegin(GL_TRIANGLE_STRIP)
		glColor3fv(cores[random.choice(range(len(cores)))])
		phi = 0.0
		while phi <= (math.pi * 2):
			glVertex3fv(s(delta, phi))
			glVertex3fv(s(delta + aux, phi))				
			phi += aux
		glVertex3fv(s(delta, 0.0))
		glVertex3fv(s(delta+aux, 0.0))
		glEnd()
		delta += aux

	contador += 0.1

def draw():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,0,0,10)
    polygonRevolucao()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("REVOLUCAO")
glutDisplayFunc(draw)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-8)
glRotatef(90,1,0,0)
glutTimerFunc(50,timer,1)
glutMainLoop()
