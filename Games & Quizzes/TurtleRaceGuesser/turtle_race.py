from turtle import Turtle, Screen
import random
is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

y_positions = [-70, -40, -10, 20, 50, 80]

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} is the winner!")
            else:
                print(f"You've lost! The {winning_color} is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


# tom = Turtle(shape="turtle")
# tom.color(colors[1])
# tom.penup()
# tom.goto(x=-230, y=-50)
#
# tam = Turtle(shape="turtle")
# tam.color(colors[2])
# tam.penup()
# tam.goto(x=-230, y=0)
#
# tum = Turtle(shape="turtle")
# tum.color(colors[3])
# tum.penup()
# tum.goto(x=-230, y=50)
#
# tem = Turtle(shape="turtle")
# tem.color(colors[4])
# tem.penup()
# tem.goto(x=-230, y=100)
#
# tym = Turtle(shape="turtle")
# tym.color(colors[5])
# tym.penup()
# tym.goto(x=-230, y=150)



screen.exitonclick()