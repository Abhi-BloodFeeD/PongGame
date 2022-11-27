import turtle
import random

from paddle import Paddle, Ball, Pen


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

# Score
pen = Pen(0)


# Keyboard Bindings
wn.listen()

# Panal A
wn.onkeypress(paddle_a.move_up, "w")
wn.onkeypress(paddle_a.move_down, "s")

# Panal B
wn.onkeypress(paddle_b.move_up, "Up")
wn.onkeypress(paddle_b.move_down, "Down")
# Main Game loop
player_1 = 0
player_2 = 0
ball.element.dx = random.choice([-2, 2])
ball.element.dy = random.choice([-2, 2])

while True:
    wn.update()

    # Move ball

    ball.element.setx(ball.element.xcor()+ball.element.dx)
    ball.element.sety(ball.element.ycor()+ball.element.dy)

    # Border check
    if (ball.element.ycor() > 340):
        ball.element.sety(340)
        ball.element.dy *= -1
    if (ball.element.ycor() < -340):
        ball.element.sety(-340)
        ball.element.dy *= -1
    if (ball.element.xcor() > 440):
        ball.element.goto(0, 0)
        ball.element.dx = random.choice([-2, 2])
        player_1 += 1
        pen.element.clear()
        pen.write_score(player_1, player_2)
    if (ball.element.xcor() < -440):
        ball.element.goto(0, 0)
        ball.element.dx = random.choice([-2, 2])
        player_2 += 1
        pen.element.clear()
        pen.write_score(player_1, player_2)
    # collission

    if (ball.element.xcor() > 390 and ball.element.xcor() < 450) and (ball.element.ycor() < paddle_b.element.ycor()+50 and ball.element.ycor() > paddle_b.element.ycor()-50):
        ball.element.setx(390)
        ball.element.dx *= -1

    if (ball.element.xcor() < -390 and ball.element.xcor() > -450) and (ball.element.ycor() < paddle_a.element.ycor()+50 and ball.element.ycor() > paddle_a.element.ycor()-50):
        ball.element.setx(-390)
        ball.element.dx *= -1
