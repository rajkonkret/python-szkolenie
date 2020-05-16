import turtle
def create_window():
    window = turtle.Screen()#ekran
    window.title('Pong Akademia Kodu')#tytul
    window.bgcolor('black')#kolor ekranu
    window.setup(width=800,height=600)
    window.tracer(0)#szybkosc odswiezania
    return window
def create_paddle(x,y):
    paddle = turtle.Turtle()#tworzy jeden element do rysowania
    paddle.speed(0)
    paddle.shape("square")#tworzy prostokat
    paddle.color('white')
    paddle.shapesize(stretch_wid=5, stretch_len=1)#rozmiar
    paddle.penup()#nie ma sladow zolwika
    paddle.goto(x,y)
    return paddle
def create_ball():
    ball = turtle.Turtle() 
    ball.speed(0)
    ball.shape("circle") 
    ball.shapesize(stretch_wid=1,stretch_len=1)
    ball.color("white") 
    ball.goto(0,0)
    ball.penup()
    return ball
window = create_window()
paddle_left = create_paddle(-350,0)
paddle_right = create_paddle(350,0)
ball = create_ball()
window.listen()

def paddle_left_change(distance):
    y = paddle_left.ycor()
    y +=distance
    paddle_left.sety(y)
def paddle_left_up():
    paddle_left_change(20)
def paddle_left_down():
    paddle_left_change(-20)
window.onkeypress(paddle_left_up,"w")
window.onkeypress(paddle_left_down,"s")
def paddle_right_change(distance):
    y = paddle_right.ycor()
    y +=distance
    paddle_right.sety(y)
def paddle_right_up():
    paddle_right_change(20)
def paddle_right_down():
    paddle_right_change(-20)
window.onkeypress(paddle_right_up,"Up")
window.onkeypress(paddle_right_down,"Down")
# Up , Down
#while True:
#window.update()
ball.dx = 2
ball.dy = -2
# Up , Down
while True:
    window.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    # zdobyccie bramki
    if ball.xcor() >390 or ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx = ball.dx*-1
    # odbijanie się piłki od krawędzi gornej i dolnej
    if ball.ycor()>290 or ball.ycor() <-290:
       ball.dy = ball.dy*-1  
    if ((ball.xcor() >340 and ball.xcor() <350) and (ball.ycor() <
        paddle_right.ycor()+40 and ball.ycor()
>paddle_right.ycor()-40)):
        ball.setx(340)
        ball.dx*=-1
    if ((ball.xcor() <-340 and ball.xcor() >-350) and (ball.ycor()
<        
        paddle_left.ycor()+40 and ball.ycor() 
>paddle_left.ycor()-40)):
        ball.setx(-340)        
        ball.dx*=-1  