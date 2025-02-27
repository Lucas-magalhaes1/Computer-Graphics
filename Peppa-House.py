from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import cos, sin, pi

def inicio():
    glClearColor(0.5, 0.8, 1, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 800, 0, 600)

def desenha_casa():
    glColor3f(1, 1, 0)
    glBegin(GL_QUADS)
    glVertex2f(200, 200)
    glVertex2f(600, 200)
    glVertex2f(600, 400)
    glVertex2f(200, 400)
    glEnd()

    glColor3f(1, 0, 0)
    glBegin(GL_TRIANGLES)
    glVertex2f(150, 400)
    glVertex2f(650, 400)
    glVertex2f(400, 500)
    glEnd()

    glColor3f(0, 1, 0)
    glBegin(GL_QUADS)
    glVertex2f(0, 200)
    glVertex2f(800, 200)
    glVertex2f(800, 0)
    glVertex2f(0, 0)
    glEnd()

    glColor3f(0.6, 0.3, 0)
    glBegin(GL_QUADS)
    glVertex2f(350, 200)
    glVertex2f(450, 200)
    glVertex2f(450, 300)
    glVertex2f(350, 300)
    glEnd()

    glColor3f(1, 1, 1)
    glBegin(GL_QUADS)
    glVertex2f(250, 330)
    glVertex2f(350, 330)
    glVertex2f(350, 380)
    glVertex2f(250, 380)
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(450, 330)
    glVertex2f(550, 330)
    glVertex2f(550, 380)
    glVertex2f(450, 380)
    glEnd()

    glColor3f(0, 0, 0)
    glBegin(GL_LINES)
    glVertex2f(300, 330)
    glVertex2f(300, 380)
    glVertex2f(250, 355)
    glVertex2f(350, 355)
    glVertex2f(500, 330)
    glVertex2f(500, 380)
    glVertex2f(450, 355)
    glVertex2f(550, 355)
    glEnd()

    glColor3f(0, 0, 0)
    glBegin(GL_QUADS)
    glVertex2f(410, 270)
    glVertex2f(420, 270)
    glVertex2f(420, 280)
    glVertex2f(410, 280)
    glEnd()

def desenha_peppa_pig():
    glColor3f(1, 0.4, 0.6)
    desenha_circulo(750, 250, 40)
    desenha_circulo(770, 290, 10)
    desenha_circulo(730, 290, 10)

    glColor3f(1, 1, 1)
    desenha_circulo(740, 260, 10)
    desenha_circulo(760, 260, 10)

    glColor3f(0, 0, 0)
    desenha_circulo(740, 265, 4)
    desenha_circulo(760, 265, 4)

    glColor3f(1, 0.2, 0.2)
    desenha_circulo(770, 245, 8)

    glColor3f(0, 0, 0)
    glBegin(GL_LINE_STRIP)
    glVertex2f(775, 240)
    glVertex2f(775, 230)
    glVertex2f(780, 225)
    glEnd()

def desenha_circulo(x, y, raio):
    num_lados = 100
    glBegin(GL_POLYGON)
    for i in range(num_lados):
        angulo = 2 * pi * i / num_lados
        xi = x + raio * cos(angulo)
        yi = y + raio * sin(angulo)
        glVertex2f(xi, yi)
    glEnd()

def desenha():
    glClear(GL_COLOR_BUFFER_BIT)
    desenha_casa()
    desenha_peppa_pig()
    glFlush()

def main():
    try:
        glutInit()
        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
        glutInitWindowPosition(100, 100)
        glutInitWindowSize(800, 600)
        glutCreateWindow(b"Cena com Casa e Peppa Pig")
    except Exception as e:
        print(f"Erro ao criar contexto OpenGL: {e}")

    inicio()
    glutDisplayFunc(desenha)
    glutMainLoop()

if __name__ == '__main__':
    main()
