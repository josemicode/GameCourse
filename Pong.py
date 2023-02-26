# Python Pong Game

import turtle

# Base Window Settings
wn = turtle.Screen()
wn.title("Retro-Pong")
wn.bgcolor("green")
wn.setup(width=500, height=500)
wn.tracer(0)

# Pad A
pad_a = turtle.Turtle()
pad_a.speed(0)
pad_a.shape("square")
pad_a.shapesize(stretch_len=0.5, stretch_wid=3)
pad_a.color("white")
pad_a.penup()
pad_a.goto(-200, 0)

# Pad B
pad_b = turtle.Turtle()
pad_b.speed(0)
pad_b.shape("square")
pad_b.shapesize(stretch_len=0.5, stretch_wid=3)
pad_b.color("white")
pad_b.penup()
pad_b.goto(200, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.shapesize(stretch_len=0.5, stretch_wid=0.5)
ball.color("white")
ball.penup()
ball.goto(25, -50)
ball.dx = 0.08
ball.dy = 0.08

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 210)
pen.write("A: 0    B: 0", align="center", font=("Times New Roman", 24, "normal"))

# Border Line
border = turtle.Turtle()
border.speed(0)
border.color("white")
border.penup()
border.goto(242, 250)
border.pendown()
border.goto(242, -250)
border.goto(-250, -250)
border.goto(-250, 250)
border.goto(242, 250)
border.hideturtle()

# Score
score_a = 0
score_b = 0


# Movement Funcs
def padup_a():
    y = pad_a.ycor()
    y += 15
    pad_a.sety(y)


def paddown_a():
    y = pad_a.ycor()
    y += -15
    pad_a.sety(y)


def padup_b():
    y = pad_b.ycor()
    y += 15
    pad_b.sety(y)


def paddown_b():
    y = pad_b.ycor()
    y += -15
    pad_b.sety(y)


# Key Binds
wn.listen()
wn.onkeypress(padup_a, "w")
wn.onkeypress(paddown_a, "s")
wn.onkeypress(padup_b, "Up")
wn.onkeypress(paddown_b, "Down")

# Main Game Loop
while True:
    try:
        wn.update()

        # Ball Movement
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border Check
        if ball.ycor() > 240:
            ball.sety(240)
            ball.dy *= -1

        if ball.xcor() > 240:
            ball.setx(0)
            ball.dx *= -1
            pen.clear()
            score_a += 1
            pen.write("A: {}    B: {}".format(score_a, score_b), align="center", font=("Times New Roman", 24, "normal"))

        if ball.ycor() < -240:
            ball.sety(-240)
            ball.dy *= -1

        if ball.xcor() < -240:
            ball.setx(0)
            ball.dx *= -1
            pen.clear()
            score_b += 1
            pen.write("A: {}    B: {}".format(score_a, score_b), align="center", font=("Times New Roman", 24, "normal"))

        # Pad Collision
        if ((ball.xcor() > 200) and (ball.ycor() > pad_b.ycor() - 45) and (ball.ycor() < pad_b.ycor() + 45)) or (
                (ball.xcor() < -200) and (ball.ycor() > pad_a.ycor() - 45) and (ball.ycor() < pad_a.ycor() + 45)):
            ball.dx *= -1

    except Exception as e:
        break