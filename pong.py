import turtle

wn = turtle.Screen()
wn.title("Tchalla games")
wn.bgcolor("black")
wn.setup(width =800, height=600)
wn.tracer(0)

#barra A

barra_A = turtle.Turtle()
barra_A.speed(0)
barra_A.shape("square")
barra_A.color("white")
barra_A.penup()
barra_A.shapesize(stretch_wid=5, stretch_len=1)
barra_A.goto(-350, 0)

# barra B 
barra_B = turtle.Turtle()
barra_B.speed(0)
barra_B.shape("square")
barra_B.color("white")
barra_B.penup()
barra_B.shapesize(stretch_wid=5, stretch_len=1)
barra_B.goto(350, 0)

# bola
 
bola = turtle.Turtle()
bola.speed(0)
bola.shape("square")
bola.color("white")
bola.penup()
bola.goto(0, 0)
bola.dx = 0.1
bola.dy = 0.1

#placar

placar = turtle.Turtle()
placar.speed(0)
placar.color("white")
placar.penup()
placar.hideturtle()
placar.goto(0, 260)
placar.write("Jogador 1: 0  Jogador 2: 0", align="center", font=("Courier", 24, "normal"))
placar_A = 0
placar_B = 0


def barra_A_cima():
    y = barra_A.ycor()
    y += 20
    
    return barra_A.sety(y) 

def barra_A_baixo():
    y = barra_A.ycor()
    y -= 20
    
    return barra_A.sety(y)

def barra_B_cima():
    y = barra_B.ycor()
    y += 20
    
    return barra_B.sety(y) 

def barra_B_baixo():
    y = barra_B.ycor()
    y -= 20
    
    return barra_B.sety(y)  
    
wn.listen()
wn.onkeypress(barra_A_cima, "w")
wn.onkeypress(barra_A_baixo, "s")
wn.onkeypress(barra_B_cima, "Up")
wn.onkeypress(barra_B_baixo, "Down")


# laço principal do jogo

while True :
    wn.update()

    #mover bola

    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    if bola.ycor() > 290 :
        bola.sety(290)
        bola.dy *= -1

    elif bola.ycor() <   -290 :
        bola.sety( -290)
        bola.dy *= -1
    
    elif bola.xcor() >  390 :
        bola.goto(0, 0)
        bola.dx *= -1
        placar_A += 1
        placar.clear()
        placar.write("Jogador 1: {}  Jogador 2: {}".format(placar_A, placar_B), align="center", font=("Courier", 24, "normal"))
    
    elif bola.xcor() <  -390 :
        bola.goto(0, 0)
        bola.dx *= -1
        placar_B += 1
        placar.clear()
        placar.write("Jogador 1: {}  Jogador 2: {}".format(placar_A, placar_B), align="center", font=("Courier", 24, "normal"))

     # parar bola reverter 

    if ((bola.xcor()) > 340 and (bola.xcor()) < 350 ) and (bola.ycor() < barra_B.ycor() + 40 and bola.ycor() > barra_B.ycor() - 40 ) :
        bola.setx(340)
        bola.dx *= -1 

    elif (bola.xcor() < -340 and bola.xcor() > -350 ) and (bola.ycor() < barra_A.ycor() + 40 and bola.ycor() > barra_A.ycor() - 40 ) :
        bola.setx(-340)
        bola.dx *= -1 



