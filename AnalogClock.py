import turtle
import time
window = turtle.Screen()
window.bgcolor('black')
window.setup(width=600, height=600)
window.title('Clock')
window.tracer(0)
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)
def draw_clock(hour, minute, second):
    pen.up()
    pen.goto(0, 210)
    pen.setheading(180)
    pen.color('green')
    pen.pendown()
    pen.circle(210)
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(90)
    for i in range(12):
        pen.fd(190)
        pen.pendown()
        if i == 0:
            pen.write(str(i + 12), font=('Courier', 24, 'bold'))
        else:
            pen.write(str(i), font=('Courier', 24, 'bold'))
        pen.fd(20)
        pen.penup()
        pen.goto(0, 0)
        pen.rt(30)
    pen.penup()
    pen.goto(0, 0)
    pen.color('white')
    pen.setheading(90)
    angle = (hour/12) * 360
    pen.rt(angle)
    pen.pensize(10)
    pen.pendown()
    pen.fd(100)
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(90)
    angle = (minute/60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(200)
    pen.penup()
    pen.goto(0, 0)
    pen.color('orange')
    pen.setheading(90)
    angle = (second/60) * 360
    pen.rt(angle)
    pen.pensize(3)
    pen.pendown()
    pen.fd(200)
while True:
    h = int(time.strftime('%I'))
    m = int(time.strftime('%M'))
    s = int(time.strftime('%S'))
    draw_clock(h, m, s)
    window.update()
    time.sleep(1)
    pen.clear()
window.mainloop()
