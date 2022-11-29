"""
APS2 — PARTE2

Nome: Victor Manuel de Barros Garcia
Matricula: 20102283

Computação Gráfica e Visão Computacional
BS — INF0601N - 2022-2
"""

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

# Tamanho da Janela - WindowSize - glutInitWindowSize(Length, Height)
Width = 1024  # Largura
Height = 600  # Altura

fAspect = 1.77
angle = 45


# Inicializa parâmetros de rendering
def Inicializa():
    """
    A função "glClearColor" que determina a cor utilizada para limpar a janela.
    Seu protótipo é: void glClearColor(GLclampf red, GLclampf green, GLclampf blue, GLclampf alfa);.
    GLclampf é definido como um float na maioria das implementações de OpenGL.
    O intervalo para cada componente red, green, blue é de 0 a 1. O componente alfa é usado para efeitos especiais,
    tal como transparência.
    """
    glClearColor(0., 0., 1., 1.)


# Função usada para especificar o volume de visualização
def EspecificaParametrosVisualizacao():
    global angle, fAspect

    # Especifica sistema de coordenadas de projeção
    glMatrixMode(GL_PROJECTION)

    # Inicializa sistema de coordenadas de projeção
    glLoadIdentity()

    # Especifica a projeção perspectiva
    # gluPerspective(40.,1.,1.,40.)
    gluPerspective(angle, fAspect, 0.4, 500)

    # Especifica sistema de coordenadas do modelo
    glMatrixMode(GL_MODELVIEW)
    # Inicializa sistema de coordenadas do modelo
    glLoadIdentity()

    # Especifica posição do observador e do alvo
    # gluLookAt(0,80,200, 0,0,0, 0,1,0);
    gluLookAt(0, 8, 20,
              0, 0, 0,
              0, 1, 0)


# Função callback chamada para gerenciar eventos do mouse
def GerenciaMouse(button, state, x, y):
    global angle

    if button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:  # Zoom-in
            if angle >= 10:
                angle -= 5
    if button == GLUT_RIGHT_BUTTON:
        if state == GLUT_DOWN:  # Zoom-out
            if angle <= 130:
                angle += 5
    EspecificaParametrosVisualizacao()
    glutPostRedisplay()


# Função callback chamada quando o tamanho da janela é alterado
def AlteraTamanhoJanela(Width, Height):
    # Para previnir uma divisão por zero
    if Height == 0:
        Height = 1

    # Especifica o tamanho da viewport
    glViewport(0, 0, Width, Height)

    # Calcula a correção de aspecto
    fAspect = Width / Height

    EspecificaParametrosVisualizacao()


def DefinirIluminacao():
    # Habilita a definição da cor do material a partir da cor corrente
    glEnable(GL_COLOR_MATERIAL)
    # Habilita o uso de iluminação
    glEnable(GL_LIGHTING)
    # Habilita a luz de número 0
    glEnable(GL_LIGHT0)
    # Habilita o depth-buffering (z-buffer)
    glEnable(GL_DEPTH_TEST)
    # Habilita o modelo de colorização de Gouraud
    glShadeModel(GL_SMOOTH)
    # outros comando
    pass


def InicializaIluminacao_1():
    glClearColor(0., 0., 0., 1.)  # Cor do fundo

    lightZeroPosition = [-20., 2., -2., 1.]
    lightZeroColor = [1.8, 1.0, 0.8, 1.0]  # green tinged
    glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
    glEnable(GL_LIGHT0)
    pass


def chao():
    glPushMatrix()
    glTranslatef(0, 0, 0)
    glScalef(6, 0.05, 5)
    glutWireCube(3.9)
    glPopMatrix()

    pass


def mesa():
    # Pé Esquerda Atrás
    glPushMatrix()
    glRotatef(40, 0, 0, 0)
    glTranslatef(-16, -1, -25)
    glScalef(1, 3, 1)
    glutWireCube(2)
    glPopMatrix()

    # Pé Direita Atrás
    glPushMatrix()
    glRotatef(40, 0, 0, 0)
    glTranslatef(8, -1, -25)
    glScalef(1, 3, 1)
    glutWireCube(2)
    glPopMatrix()

    # Pé Direita Frente
    glPushMatrix()
    glRotatef(40, 0, 0, 0)
    glTranslatef(8.2, -1, -8)
    glScalef(1, 3, 1)
    glutWireCube(2)
    glPopMatrix()


    # Pé Esquerda Frente
    glPushMatrix()
    glRotatef(40, 0, 0, 0)
    glTranslatef(-17, -1, -7)
    glScalef(1, 3, 1)
    glutWireCube(2)
    glPopMatrix()


    # Parte de cima da mesa
    glPushMatrix()
    glTranslatef(-3, 2, -10)
    glScalef(6, 0.05, 5)
    # glRotatef(40,0,0,1)
    glutWireCube(3.2)
    glPopMatrix()

    pass


def cubo():
    # cubo
    glPushMatrix()
    glRotatef(40, 0, 0, 0)
    glTranslatef(10, -1, 6)
    glScalef(4, 3, 4)
    glutWireCube(1)
    glPopMatrix()
    pass


def bule():
    glPushMatrix()
    glTranslatef(-3, 2, -10)
    glutWireTeapot(1.5)
    glPopMatrix()

    pass


def cilindro():
    glPushMatrix()
    glTranslatef(-8, 3, -10)
    glRotatef(120, -170, 180, 180)
    glutWireCylinder(2, 2, 15, 12)
    glPopMatrix()

    pass


def cabocilindro():
    glPushMatrix()
    glTranslatef(-8, 5, -10)
    glScalef(1, 4, 1)
    glutWireCube(1)
    glPopMatrix()

    pass


def cone():
    glPushMatrix()
    glTranslatef(-8, 7, -10)
    glRotatef(120, -150, 180, 180)
    glutWireCone(3.5, 1, 8, 10)
    glPopMatrix()

    pass


# Função callback chamada para fazer o desenho da mesa
def Desenha():
    # Limpa a janela e o depth buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # Define a refletância do material do objeto
    color = [1.0, 0., 0., 1.]  # Cor do objeto
    glMaterialfv(GL_FRONT, GL_DIFFUSE, color)
    # Salva as transformações atuais na pilha

    chao()
    mesa()
    cubo()
    bule()
    cilindro()
    cabocilindro()
    cone()

    # Executa os comandos OpenGL
    glutSwapBuffers()
    return


def main():
    glutInit(sys.argv)
    # Define o modo de exibição inicial
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    # Define a tamanho da janela
    glutInitWindowSize(500, 500)
    # Da o nome da janela
    glutCreateWindow("APS2-PARTE1")
    # Montar a imagem
    glutDisplayFunc(Desenha)
    '''
    Estabelece a função "AlteraTamanhoJanela" previamente definida como a função callback 
    de alteração do tamanho da janela. Isto é, sempre que a janela é maximizada, minimizada, etc., 
    a função "AlteraTamanhoJanela" é executada para reinicializar o sistema de coordenadas.
    '''
    glutReshapeFunc(AlteraTamanhoJanela)
    '''
    A função callback "glutMouseFunc" que é chamada pela GLUT cada vez que ocorre um evento de mouse. 
    Parâmetros de entrada da função callback: (int button, int state, int x, int y). 
    Três valores são válidos para o parâmetro button: 
    GLUT_LEFT_BUTTON, GLUT_MIDDLE_BUTTON e GLUT_RIGHT_BUTTON. 
    O parâmetro state pode ser GLUT_UP ou GLUT_DOWN. Os parâmetros x e y indicam a localização do mouse 
    no momento que o evento ocorreu.
    '''
    glutMouseFunc(GerenciaMouse)
    # Inicializa parâmetros de rendering
    Inicializa()
    DefinirIluminacao()
    InicializaIluminacao_1()
    '''
    A função "glutMainLoop" que faz com que comece a execução da “máquina de estados” e processa todas as mensagens 
    específicas do sistema operacional, tais como teclas e botões do mouse pressionados, 
    até que o programa termine.
    '''
    glutMainLoop()
    return


if __name__ == '__main__': main()
