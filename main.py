from turtle import Turtle, Screen

my_screen = Screen()
my_screen.setup(width=500, height=400)
user_bet = my_screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')

# print(user_bet)

colors = ['red', 'blue', 'green', 'orange', 'yellow', 'purple']

red = Turtle('turtle')
blue = Turtle('turtle')
green = Turtle('turtle')
orange = Turtle('turtle')
yellow = Turtle('turtle')
purple = Turtle('turtle')

turtles = [red, blue, green, orange, yellow, purple]

unique_color = -1
default_y = 125

for turtle in turtles:
    turtle.penup()
    unique_color += 1
    default_y -= 30
    turtle.color(colors[unique_color])
    turtle.goto(x=-230, y=default_y)

my_screen.listen()
my_screen.exitonclick()
