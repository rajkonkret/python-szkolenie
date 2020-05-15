import turtle

def paddle(x,y):
    paddle = turtle.Turtle()
    paddle.speed(0)
    paddle.shape("square")
    paddle.color("white")
    paddle.shapesize(stretch_wid=5,stretch_len=1)
    paddle.penup()
    paddle.goto(x,y)
    return paddle

def ball(x,y):
    circle = turtle.Turtle()
    circle.shape("circle")
    circle.color("red")
    circle.goto(x,y)
    circle.penup()
    return circle

def create_window():
    window = turtle.Screen()
    window.title('Pong')
    window.bgcolor('black')
    window.setup(width=800,height=600)
    window.tracer(0)
    return window

def left_paddle_change(distance):
    y = paddle_l.ycor()
    y+=distance
    if y in range(-250,250):
        paddle_l.sety(y)

def right_paddle_change(distance):
    y = paddle_r.ycor()
    y+=distance
    if y in range(-250,250):
        paddle_r.sety(y)

def paddle_l_up():
    left_paddle_change(20)

def paddle_l_down():
    left_paddle_change(-20)

def paddle_r_up():
    right_paddle_change(20)

def paddle_r_down():
    right_paddle_change(-20)

window = create_window()
window.listen()
ball_c = ball(0,0)
paddle_r = paddle(350,0)
paddle_l = paddle(-350,0)

ball_c.dx = 2
ball_c.dy = -2

window.onkeypress(paddle_l_up,"w")
window.onkeypress(paddle_l_down,"s")
window.onkeypress(paddle_r_up,"Up")
window.onkeypress(paddle_r_down,"Down")

while True:
    window.update()
    ball_c.setx(ball_c.xcor()+ball_c.dx)
    ball_c.sety(ball_c.ycor()+ball_c.dy)

    if ball_c.xcor() > 390 or ball_c.xcor() < -390:
       ball_c.goto(0,0)
       ball_c.dx = -ball_c.dx
       print("gool!")

    if ball_c.ycor() > 290 or ball_c.ycor() < -290:
       #ball_c.goto(0,0)
       ball_c.dy = -ball_c.dy
    
    if ball_c.xcor() == paddle_l.xcor() and abs(paddle_l.ycor()-ball_c.ycor()) < 80:
        print("gooola nie ma....")
        print(paddle_l.ycor())
        ball_c.dx = -ball_c.dx

    if ball_c.xcor() == paddle_r.xcor() and abs(paddle_r.ycor()-ball_c.ycor()) < 80:
        print("gooola nie ma....")
        print(paddle_r.ycor())
        ball_c.dx = -ball_c.dx


