import pygame
import time
import random

pygame.init()
reloj = pygame.time.Clock()

c_amarillo = (255, 255, 0)
c_negro = (0,0,0)
c_rojo = (213,0,0)
c_verde = (0,255,0)
c_azul = (0, 102, 255)

display_ancho = 600
display_alto = 400

ser_bloque = 10
ser_list=[]


disp = pygame.display.set_mode((display_ancho, display_alto))
pygame.display.set_caption("Juego Snake")  # Nombre para display

#Define la estructura de la serpiente y posicion
def serpiente(ser_bloque, ser_list):
    for x in ser_list:
        pygame.draw.rect(disp, c_negro, [x[0], x[1], ser_bloque, ser_bloque])

#Funcion principal

def eljuego():

    comidax = round(random.randrange(0, display_ancho - ser_bloque) / 10.0) * 10.0
    comiday = round(random.randrange(0, display_alto - ser_bloque) / 10.0) * 10.0

    #Coordenadas de inicio
    x1= display_ancho/2
    y1= display_ancho/2

    #Coordenandas cambio

    x1c=0
    y1c=0

    #Lista para el crecimiento de la snake

    ser_list=[]
    largo_ser=1


    j_acabado= False    #Para cerrar el juego
    j_terminado = False  #El usuario perdio

    while not j_acabado: #Ciclo para que no cierre el programa
        #Para mostrar el puntaje
        while j_terminado == True:
            puntaje= largo_ser-1
            puntaje_fuente = pygame.font.SysFont("arial", 32)
            valor= puntaje_fuente.render("Su puntaje es: " + str(puntaje), True, c_rojo)
            disp.blit(valor, [display_ancho/3, display_alto/5])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    j_acabado=True
                    j_terminado=False

        for event in pygame.event.get(): ## revisar este for
            if event.type == pygame.QUIT:
                j_acabado = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1c = -ser_bloque
                    y1c = 0
                elif event.key == pygame.K_RIGHT:
                    x1c = ser_bloque
                    y1c = 0
                elif event.key == pygame.K_UP:
                    x1c = 0
                    y1c = -ser_bloque
                elif event.key == pygame.K_DOWN:
                    x1c = 0
                    y1c = ser_bloque
        if x1>=display_ancho or  x1<0  or  y1>=display_alto  or  y1<0:
            j_terminado= True
        # Coordinadas de cambio
        x1 = x1+ x1c
        y1 = y1+ y1c
        disp.fill(c_azul) #Fondo color
        pygame.draw.rect(disp,c_amarillo,[comidax,comiday,ser_bloque,ser_bloque]) #Comida
        ser_cabeza = []
        ser_cabeza.append(x1)
        ser_cabeza.append(y1)
        ser_list.append(ser_cabeza)

        #Condiciones para terminar
        #Cuando la serpiente excede
        if len(ser_list) > largo_ser:
            del ser_list[0]

        #Cuando la serpiente se pega con ella misma
        for x in ser_list: #para no darse con el ultimo bloque
            if x == ser_list:
                j_terminado = True
        serpiente(ser_bloque, ser_list)

        #Cuando la serpiente come
        if x1 == comidax and y1 == comiday:
            comidax= round(random.randrange(0, display_ancho - ser_bloque) / 10.0) * 10.0
            comiday= round(random.randrange(0, display_alto - ser_bloque) / 10.0) * 10.0
            largo_ser +=1

        reloj.tick(10)



        pygame.display.update()
    pygame.quit()
    quit()

eljuego()