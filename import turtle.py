import turtle

t = turtle.Turtle()

def square(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    for _ in range(4):
        t.forward(100)
        t.right(90)

square(0, 0)
turtle.done()
                