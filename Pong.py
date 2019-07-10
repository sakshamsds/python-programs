# Simple Pong in Python 3 for Beginners in Functional Style
# By @TokyoEdTech
# Part 1: Getting Started
# Part 2: Adding Game Objects i.e., paddles and ball
# Part 3: Moving the paddles
# Part 4: Moving the ball
# Part 5: Colliding with the paddles
# Part 6: Scoring 
# Part 7: Sounds
# Part 8: Personalization

import turtle
import winsound

win = turtle.Screen()
win.title('Pong by @TokyoEdTech')
win.bgcolor('black')                # Background color
win.setup(width=800, height=600)
win.tracer(0)                       # Stops window from automatically updating cuz its slower

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)                   # Not the speed with which the paddle moves but the speed of animation which is set to max
paddle_a.shape('square')            # By default 20*20 pixel
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()                    # dont want to draw a line while moving
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 0.4
ball.dy = 0.3

# Center Line
center_line = turtle.Turtle()
center_line.speed(0)
center_line.shape('square')
center_line.color('white')
center_line.shapesize(stretch_wid=25, stretch_len=0.1)
center_line.penup()
center_line.goto(0, 0)

# Pen 
pen = turtle.Turtle()
pen.speed(0)   
pen.color('white') 
pen.penup()
pen.hideturtle()
pen.goto(0, 260)            
pen.write('Player A: 0    Player B: 0', align='center', font=('Courier', 28, "normal"))

# Functions for moving paddle
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard Binding
win.listen()                        # getting input from keyboard
win.onkeypress(paddle_a_up, 'w')
win.onkeypress(paddle_a_down, 's')
win.onkeypress(paddle_b_up, 'Up')
win.onkeypress(paddle_b_down, 'Down')


# Main game loop
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor() > 290:
        # ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound('unsure.wav', winsound.SND_ASYNC)

    if ball.ycor() < -290:
        # ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound('unsure.wav', winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write('Player A: {}    Player B: {}'.format(score_a, score_b), align='center', font=('Courier', 28, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write('Player A: {}    Player B: {}'.format(score_a, score_b), align='center', font=('Courier', 28, 'normal'))

    # Paddle and Ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor()+50 and ball.ycor() > paddle_b.ycor()-50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound('unsure.wav', winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() < -350) and (ball.ycor() < paddle_a.ycor()+50 and ball.ycor() > paddle_a.ycor()-50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound('unsure.wav', winsound.SND_ASYNC)
