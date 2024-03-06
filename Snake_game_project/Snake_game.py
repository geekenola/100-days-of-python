from turtle import Turtle, Screen

screen = Screen()
screen.setup(width = 600, height = 600)

screen.bgcolor("black")
screen.title("My Snake Game")



staring_positions = [(0,0), (-20, 0), (-40, 0)]

for i in range(3):
    tim = Turtle()
    tim.shape("square")
    tim.color("white")
    tim.goto(staring_positions[i])


screen.exitonclick()