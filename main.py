import turtle
t=turtle.Turtle()
s=turtle.Screen()
s.setup(850,800)
s.bgcolor('black')
t.color('violet')
t.begin_fill()
t.penup()
t.left(110)
t.fd(50)
t.pendown()
t.speed(0)
t.circle(30)
t.penup()
t.backward(150)
t.pendown()
t.lt(10)
t.fd(90)
t.lt(50)
t.fd(10)
t.lt(10)
t.fd(58)
t.lt(70)
t.fd(90)
t.lt(90)
t.fd(20)
t.lt(90)
t.fd(70)
t.rt(80)
t.fd(6)
t.rt(99)
t.fd(130)
t.lt(105)
t.fd(30)
t.rt(85)
t.fd(80)
t.lt(90)
t.fd(20)
t.lt(90)
t.fd(80)
t.rt(90)
t.fd(30)
t.rt(90)
t.fd(80)
t.lt(90)
t.fd(20)
t.lt(90)
t.fd(80)
t.rt(90)
t.fd(30)
t.lt(110)
t.fd(130)
t.rt(99)
t.fd(6)
t.rt(80)
t.fd(67)
t.lt(88)
t.fd(25)
t.end_fill()
t.penup()
t.goto(-140,85)
t.pendown()
t.color('yellow')
t.write("HAPPY",align="center",font=("arial",49,"bold"))
t.penup()
t.goto(-110,-10)
t.pendown()
t.color('lightblue')
t.write("M",align="center",font=("arial",59,"bold"))
t.penup()
t.goto(-10,-10)
t.pendown()
t.color('lightblue')
t.write("THER'S",font=("arial",49,"bold"))
t.penup()
t.goto(65,-111)
t.pendown()
t.color('red')
t.write("DAY",font=("arial",49,"bold"))
t.penup()
t.goto(-205,-120)
t.pendown()
t.color("yellow","tomato")
t.begin_fill()
for i in range(60):
    t.fd(100)
    t.lt(165)
t.end_fill()
t.penup()
t.goto(-185,5)
t.pendown()
t.color("red","green")
t.begin_fill()
for i in range(60):
    t.fd(85)
    t.lt(165)
t.end_fill()
t.penup()
t.goto(-310,29)
t.pendown()
t.color("blue","magenta")
t.begin_fill()
for i in range(60):
    t.fd(70)
    t.lt(165)
t.end_fill()
t.penup()
t.goto(-300,120)
t.pendown()
t.color("yellow","cyan")
t.begin_fill()
for i in range(60):
    t.fd(55)
    t.lt(165)
t.end_fill()
t.color('cyan')
t.penup()
t.goto(75,-170)
t.pendown()
t.write("Thinking Of you,",font=("italic",19))
t.penup()
t.goto(75,-230)
t.pendown()
t.write("And Hoping You,",font=("arial",19))
t.penup()
t.goto(75,-260)
t.pendown()
t.write("Have a beautiful day,",font=("arial",19))
t.penup()
t.goto(75,-290)
t.pendown()
t.write("From your loving son",font=("arial",19))
t.penup()
t.goto(75,-330)
t.pendown()
t.color('yellow')
t.write("Gouranga !!!!!",font=("arial",21))
t.width(10)
t.penup()
t.fd(200)
t.lt(69)
t.fd(470)
turtle.exitonclick()