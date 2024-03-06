from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:
    def __init__(self):
        super.__init__()
        self.penup()
        self.goto(0, -280)


    def go_up(self):
        new_y = self.ycor()+ MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
    
    
