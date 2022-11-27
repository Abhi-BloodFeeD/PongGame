
import turtle


class Element:
    def __init__(self, position):
        self.element = turtle.Turtle()
        self.element.speed(0)
        self.element.shape("square")
        self.element.color("white")
        self.element.penup()
        self.element.goto(position, 0)

    def move_up(self):
        y = self.element.ycor()
        y += 20
        y = min(300, y)
        self.element.sety(y)

    def move_down(self):
        y = self.element.ycor()
        y -= 20
        y = max(-300, y)
        self.element.sety(y)


class Ball(Element):
    def __init__(self, position):
        super().__init__(position)
        self.element.dx = 2
        self.element.dy = 2


class Paddle(Element):
    def __init__(self, position):
        super().__init__(position)
        self.element.shapesize(stretch_wid=5, stretch_len=1)
