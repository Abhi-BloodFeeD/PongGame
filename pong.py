import turtle

from paddle import Paddle, Element, Ball


wn = turtle.Screen()

wn.title("Game Developed by Abhinav Bhardwaj")
wn.bgcolor("black")
wn.setup(width=900, height=700)
wn.tracer(0)


# Panal A
paddle_a = Paddle(-400)

# Panal B
paddle_b = Paddle(400)

# Ball
ball = Ball(0)

# functions


# Keyboard Bindings
wn.listen()

# Panal A
wn.onkeypress(paddle_a.move_up, "w")
wn.onkeypress(paddle_a.move_down, "s")

# Panal B
wn.onkeypress(paddle_b.move_up, "Up")
wn.onkeypress(paddle_b.move_down, "Down")
# Main Game loop

while True:
    wn.update()

    # Move ball

    ball.setx()
