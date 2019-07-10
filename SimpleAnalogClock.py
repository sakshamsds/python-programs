# Simple Analog Clock in Python 3
# by @TokyoEdTech
# Part 1: Getting Started
# Part 2: Drawing a clock face
# Part 3: Drawing the hands
# Part 4: Updating the time

import turtle
import time

wn = turtle.Screen()
wn.bgcolor('black')
wn.setup(width=600, height=600)
wn.title('Simple Analog Clock')
wn.tracer(0)

# Create our drawing pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)          # width of line

def draw_clock(h, m, s, pen):

    # Draw the clock face
    pen.penup()
    pen.goto(0, 210)
    pen.setheading(180)
    pen.color('green')
    pen.pendown()
    pen.circle(210)
    
    # Draw the lines for seconds
    #pen.color('gold')
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(90)
    for _ in range(60):
        pen.fd(200)
        pen.pendown()
        pen.fd(5)
        pen.penup()
        pen.goto(0, 0)
        pen.rt(6)
    
    # Draw the lines for hours
    #pen.color('green')
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(90)
    for _ in range(12):
        pen.fd(185)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0, 0)
        pen.rt(30)
    
    # Draw the numbers for hours
    pen.color('white')
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(90)
    pen.rt(30)                  
    for i in range(12):
        pen.fd(160)
        pen.write(i+1, font=('Courier', 10, 'normal'))
        pen.goto(0, 0)
        pen.rt(30)
    
    # Draw the hour hand
    pen.penup()
    pen.goto(0, 0)
    pen.color('red')
    pen.setheading(90)
    angle = (h/12)*360 + (m/60)*30              # 1 hours makes 30 degre angle
    pen.rt(angle)
    pen.pendown()
    pen.fd(100)

    # Draw the minute hand
    pen.penup()
    pen.goto(0, 0)
    pen.color('blue')
    pen.setheading(90)
    angle = (m/60)*360 + (s/60)*6               # 1 minute makes 6 degree angle
    pen.rt(angle)
    pen.pendown()
    pen.fd(180)

    # Draw the second hand
    pen.penup()
    pen.goto(0, 0)
    pen.color('gold')
    pen.setheading(90)
    angle = (s/60)*360
    pen.rt(angle)
    pen.pendown()
    pen.fd(50)

    # Get the digital time
    pen.penup()
    pen.goto(0, 250)
    pen.color('white')
    pen.write('{}h : {}m : {}s'.format(h, m, s), align='center', font=('Courier', 20, 'bold'))

while True:
    # Getting the current time 
    h = int(time.strftime('%I'))
    m = int(time.strftime('%M'))
    s = int(time.strftime('%S'))

    draw_clock(h, m, s, pen)
    wn.update()
    time.sleep(1)
    pen.clear()

wn.mainloop()