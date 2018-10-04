from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import cos, sin, pi, tan
import png

cores = [ [1,0,0],[1,1,0],[0,1,0],[0,1,1],[0,0,1],[1,0,1],[0.5,1,1],[1,0,0.5], [1,0,0.2], [0.2,1,0.5]]

def LoadTextures():
    global texture
    texture = glGenTextures(1)

	################################################################################
    glBindTexture(GL_TEXTURE_2D, texture)
    reader = png.Reader(filename='renato.png')
    w, h, pixels, metadata = reader.read_flat()
    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    ################################################################################

def InitGL(Width, Height):             
    LoadTextures()
    glEnable(GL_TEXTURE_2D)
    glClearColor(0.0, 0.0, 0.0, 0.0)    
    glClearDepth(1.0)                  
    glDepthFunc(GL_LESS)               
    glEnable(GL_DEPTH_TEST)            
    glShadeModel(GL_SMOOTH)            
    
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)

def MarxistFunction(theta, phi, r):
    return [r*cos(phi)*cos(theta), r*sin(phi), r*cos(phi)*sin(theta)]

def Revolucion():
    glBindTexture(GL_TEXTURE_2D, texture)
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
            glTexCoord2f(theta/2*pi, (phi + pi/2) / pi)
            glVertex3fv(MarxistFunction(theta, phi, 1))

            glTexCoord2f((theta/2*pi) + delta, (phi + pi/2) / pi)
            glVertex3fv(MarxistFunction(theta + delta, phi, 1))

            glTexCoord2f((theta/2*pi) + delta, ((phi + pi/2) / pi) + delta)
            glVertex3fv(MarxistFunction(theta + delta, phi + delta, 1))

            glTexCoord2f(theta/2*pi, ((phi + pi/2) / pi) + delta)
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

