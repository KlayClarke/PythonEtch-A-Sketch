from turtle import Turtle, Screen
import random

my_screen = Screen()
my_screen.setup(width=500, height=400)
is_race_on = False
user_bet = my_screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')

if user_bet:
    is_race_on = True

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

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            if user_bet == turtle:
                print(f'You won. {winning_color} was the winning turtle.')
            else:
                print(f'You lose. {winning_color} was the winning turtle.')
        rand_distance = random.randint(0, 10)
        rand_turtle = random.choice(turtles)
        rand_turtle.forward(rand_distance)

my_screen.listen()
my_screen.exitonclick()
