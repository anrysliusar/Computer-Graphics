from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

rotationX = 0.0
rotationY = 0.0
amb = (0.8, 0.8, 0.8, 0.5)
posOfLight = (0, 10, 10)


def init():
    glClearColor(0, 0, 0, 1.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)
    glRotatef(-90, 1.0, 0.0, 0.0)
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, amb)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, posOfLight)
    glLightModeli(GL_LIGHT_MODEL_TWO_SIDE, GL_TRUE)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)


def Hotkeys(key, x, y):
    global rotationX
    global rotationY
    if key == GLUT_KEY_UP:
        rotationX -= 3.0
    if key == GLUT_KEY_DOWN:
        rotationX += 3.0
    if key == GLUT_KEY_LEFT:
        rotationY -= 3.0
    if key == GLUT_KEY_RIGHT:
        rotationY += 3.0
    glutPostRedisplay()


def draw():
    # pyramid
    size = 0.4

    firstColor = (1, 0, 1, 1)
    secondColor = (1, 0, 0, 1)
    thirdColor = (0, 0, 1, 1)
    fourthColor = (0.1, 1, 0, 1)
    fifthColor = (1, 1, 0, 1)


    def buildQuad(side, type, color, point1, point2, point3, point4):
        glBegin(GL_QUADS)
        glMaterialfv(side, type, color)
        glVertex3d(point1[0], point1[1], point1[2])
        glVertex3d(point2[0], point2[1], point2[2])
        glVertex3d(point3[0], point3[1], point3[2])
        glVertex3d(point4[0], point4[1], point4[2])
        glEnd()

    def buildTriangle(side, type, color, point1, point2, point3):
        glBegin(GL_TRIANGLES)
        glMaterialfv(side, type, color)
        glVertex3d(point1[0], point1[1], point1[2])
        glVertex3d(point2[0], point2[1], point2[2])
        glVertex3d(point3[0], point3[1], point3[2])
        glEnd()


    def drawQuadTetrahedron():
        # front side
        buildTriangle(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, firstColor,
                     [0, 0, 0], [size, 0, 0], [size / 2, size / 2, size / 2])
        # back side
        buildTriangle(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, secondColor,
                     [0, size, 0], [size, size, 0], [size / 2, size / 2, size / 2])
        # left side
        buildTriangle(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, thirdColor,
                     [0, 0, 0], [0, size, 0], [size / 2, size / 2, size / 2])
        # right side
        buildTriangle(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, fourthColor,
                     [size, 0, 0], [size, size, 0], [size / 2, size / 2, size / 2])
        # bottom
        buildQuad(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, fifthColor, [0, 0, 0], [size, 0, 0], [size, size, 0], [0, size, 0])

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glRotatef(rotationX, 1.0, 0.0, 0.0)
    glRotatef(rotationY, 0.0, 1.0, 0.0)
    glLightfv(GL_LIGHT0, GL_POSITION, posOfLight)

    drawQuadTetrahedron()
    glTranslatef(0.2, 0.2, 0.5)

    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, secondColor)
    glutSolidSphere(0.1, 50, 50)
    glTranslatef(0.5, -0.4, -0.3)

    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, fourthColor)
    glutSolidCone(0.3, 0.5, 40, 50)
    glTranslatef(-1.2, 0.8, -0.5)
    glPopMatrix()
    glutSwapBuffers()


# MAIN BLOCK
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(800, 800)
glutInitWindowPosition(50, 50)
glutInit(sys.argv)
glutCreateWindow("Module Control Work")
glutDisplayFunc(draw)
glutSpecialFunc(Hotkeys)
init()
glutMainLoop()
