import turtle
win = turtle.Screen()
sqare = turtle.Turtle() # zmienna na której możemy rysować
sqare.hideturtle()
sqare.back(50)
for i in range(0,4):
    sqare.forward(100)
    sqare.left(90)

sqare.left(45)
for i in range(0,4):
    sqare.left(90)
    sqare.forward(100)
    

win.mainloop()

