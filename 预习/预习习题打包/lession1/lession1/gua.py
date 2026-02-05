import turtle
# 暂时不需要知道

def jump(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def forward(l):
    turtle.forward(l)


def right(a):
    turtle.right(a)


def pause():
    turtle.done()
