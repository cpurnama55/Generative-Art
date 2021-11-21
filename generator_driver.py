import turtle                   # Turtle is included in Python3 standard library! No need to install
#import PIL                  

turtle.setup(500, 500)
turtle.Screen()
turtle.title("Turtle Keys")
move = turtle.Turtle()
# turtle.showturtle()           # Creates a duplicate idle turtle

def k1():
    move.forward(10)

def k2():
    move.left(10)

def k3():
    move.right(10)

def k4():
    move.back(10)

turtle.onkeypress(k1, "Up")
turtle.onkeypress(k2, "Left")
turtle.onkeypress(k3, "Right")
turtle.onkeypress(k4, "Down")

turtle.listen()
turtle.mainloop()