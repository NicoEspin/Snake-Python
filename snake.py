
from cgitb import text
import turtle
import time
import random
posponer=0.1

#Score
score=0
highScore=0
#Config de la Ventana
wn= turtle.Screen()
wn.title("Snake ")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

#Cabeza de serpiente
cabeza=turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction="stop"
cabeza.color("white")

#Manzanas
manzana=turtle.Turtle()
manzana.speed(0)
manzana.shape("circle")
manzana.penup()
manzana.goto(0,100)
manzana.color("red")

#Cuerpo
segmentos=[]

#Puntuacion
texto=turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("score: 0       High Score: 0", align="center", font=("Courier", 24, "normal"))
#Funciones
def arriba():
    cabeza.direction="up"

def abajo():
    cabeza.direction="down"

def izquierda():
    cabeza.direction="left"

def derecha():
    cabeza.direction="right"


def mov():
    if cabeza.direction=="up":
         y=cabeza.ycor()
         cabeza.sety(y + 20)
    
    if cabeza.direction=="down":
         y=cabeza.ycor()
         cabeza.sety(y - 20)
    
    if cabeza.direction=="left":
         x=cabeza.xcor()
         cabeza.setx(x - 20)
    
    if cabeza.direction=="right":
         x=cabeza.xcor()
         cabeza.setx(x + 20) 
#Teclado
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")
while True:
    wn.update()
    
    #Colicion bordes
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 290 or cabeza.ycor() < -280:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction="stop"

        #Borrar segmentos
        for segmento in segmentos:
            segmento.goto(1000,1000)
        segmentos.clear()    
        #Resetear score
        score=0
        texto.clear()
        texto.write("score: {}       High Score: {}".format(score,highScore), align="center", font=("Courier", 24, "normal"))

    #Colicion comida
    if cabeza.distance(manzana)< 20:
        x =random.randint(-280,280)
        y =random.randint(-280,280)
        manzana.goto(x,y)
        
        nuevo_segmento=turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.penup()
        nuevo_segmento.color("grey")
        segmentos.append(nuevo_segmento)
        #Aumentar score
        score += 10
        if score>highScore:
            highScore = score
        texto.clear()
        texto.write("score: {}       High Score: {}".format(score,highScore), align="center", font=("Courier", 24, "normal"))     
    #Mover el cuerpo
    totalSeg= len(segmentos)
    for index in range (totalSeg -1, 0, -1):
        x=segmentos[index-1].xcor()
        y=segmentos[index-1].ycor()
        segmentos[index].goto(x,y)

    #Colicion cuerpo 
    for segmento in segmentos:
        if segmento.distance(cabeza)< 20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction= "stop"
            for segmento in segmentos:
                segmento.goto(1000,1000)
            segmentos.clear()
            #Resetear score
            score=0
            texto.clear()
            texto.write("score: {}       High Score: {}".format(score,highScore), align="center", font=("Courier", 24, "normal"))   
    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)
    
    mov()
    time.sleep(posponer)