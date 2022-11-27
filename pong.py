import turtle
wn = turtle.Screen()

wn.title("Game Developed by Abhinav Bhardwaj")
wn.bgcolor("black")
wn.setup(width=900, height=750)
wn.tracer(0)


# Panal A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-400, 0)

# Panal B

# Ball
# Main Game loop

while True:
    wn.update()
