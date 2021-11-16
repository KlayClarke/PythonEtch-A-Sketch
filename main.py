from turtle import Turtle, Screen

tim = Turtle()


def create_turtle():
    tim.shape('turtle')
    tim.color('burlywood')
    tim.width(9)
    tim.speed('fastest')


create_turtle()


def forward():
    tim.forward(10)


def backward():
    tim.back(10)


def turn_left():
    tim.left(5)


def turn_right():
    tim.right(5)


def clear():
    tim.reset()
    create_turtle()


def move(func):
    return func


my_screen = Screen()
my_screen.listen()
my_screen.onkeypress(key='w', fun=move(forward))
my_screen.onkeypress(key='s', fun=move(backward))
my_screen.onkeypress(key='a', fun=move(turn_left))
my_screen.onkeypress(key='d', fun=move(turn_right))
my_screen.onkeypress(key='c', fun=move(clear))
my_screen.exitonclick()
