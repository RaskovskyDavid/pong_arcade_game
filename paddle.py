from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, coordinates):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(coordinates)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


'''paddle = Turtle()
paddle.shape("square")
# stretch_len amd stretch_wid values are going to multiply by 20
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.color("white")
paddle.penup()
paddle.goto(350, 0)'''
