import turtle
try:
    window = turtle.Screen()
    window.title('Pong🏓')
    window.bgcolor('black')
    window.setup(width=800, height=600)
    window.tracer(0)
    paddlea = turtle.Turtle()
    paddlea.speed(0)
    paddlea.shape('square')
    paddlea.color('white')
    paddlea.shapesize(stretch_wid=5, stretch_len=1)
    paddlea.penup()
    paddlea.goto(-350, 0)
    paddleb = turtle.Turtle()
    paddleb.speed(0)
    paddleb.shape('square')
    paddleb.color('white')
    paddleb.shapesize(stretch_wid=5, stretch_len=1)
    paddleb.penup()
    paddleb.goto(350, 0)
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape('square')
    ball.color('white')
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 0.1
    ball.dy = 0.1
    ascore = 0
    bscore = 0
    def move_paddlea_up():
        y = paddlea.ycor()
        y += 20
        paddlea.sety(y)
    def move_paddlea_down():
        y = paddlea.ycor()
        y -= 20
        paddlea.sety(y)
    def move_paddleb_up():
        y = paddleb.ycor()
        y += 20
        paddleb.sety(y)
    def move_paddleb_down():
        y = paddleb.ycor()
        y -= 20
        paddleb.sety(y)
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color('white')
    pen.penup()
    pen.hideturtle()
    pen.goto(-150, 260)
    pen.write(f'Player A: {ascore} Player B: {bscore}', font=('Courier', 24, 'bold'))
    window.listen()
    window.onkeypress(move_paddlea_up, 'w')
    window.onkeypress(move_paddlea_down, 's')
    window.onkeypress(move_paddleb_up, 'Up')
    window.onkeypress(move_paddleb_down, 'Down')
    while True:
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
        elif ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            ascore += 1
            pen.clear()
            pen.write(f'Player A: {ascore} Player B: {bscore}', font=('Courier', 24, 'bold'))
        elif ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            bscore += 1
            pen.clear()
            pen.write(f'Player A: {ascore} Player B: {bscore}', font=('Courier', 24, 'bold'))
        if ball.xcor() > 340  and ball.xcor() > 350 and ball.ycor() < paddleb.ycor() + 40 and ball.ycor() > paddleb.ycor() - 40:
            ball.setx(340)
            ball.dx *= -1
        if ball.xcor() < -340  and ball.xcor() < -350 and ball.ycor() < paddlea.ycor() + 40 and ball.ycor() > paddlea.ycor() - 40:
            ball.setx(-340)
            ball.dx *= -1
        window.update()
except:
    pass
