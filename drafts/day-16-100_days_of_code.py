from turtle import Turtle, Screen

tim = Turtle()

screen = Screen()

def move_right():
    tim.setheading(0)
    tim.forward(10)

def move_left():
    tim.setheading(180)
    tim.forward(10)

def move_straight():
    tim.setheading(90)
    tim.forward(10)

def move_back():
    tim.setheading(270)
    tim.forward(10)

screen.listen()
screen.onkey(key="d", fun=move_right)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="w", fun=move_straight)
screen.onkey(key="s", fun=move_back)

screen.exitonclick()

