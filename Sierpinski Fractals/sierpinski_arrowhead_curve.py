# draws Sierpinski arrowhead curve
# credit for C++ code: https://en.wikipedia.org/wiki/Sierpi%C5%84ski_curve

import turtle

def draw_curve(order, length, angle, tr_turtle): 
    if order == 0:
        tr_turtle.forward(length)
    else:
        draw_curve(order - 1, length / 2, -angle, tr_turtle)
        tr_turtle.rt(angle)
        draw_curve(order - 1, length / 2, angle, tr_turtle)
        tr_turtle.rt(angle)
        draw_curve(order - 1, length / 2, -angle, tr_turtle)


def sierpinski_arrowhead_curve(startx, starty, order, length, tcolor):
    t1 = turtle.Turtle()
    t1.color(tcolor)
    angle = 60

    t1.penup()
    t1.setpos(startx, starty)
    t1.pendown()
    
    if order % 2 == 0:
        draw_curve(order, length, angle, t1)
    else:
        t1.rt(angle)
        draw_curve(order, length, angle, t1)

screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.delay(0)
screen.tracer(0)

# change these parameters for different results
startx = -250
starty = 160
order = 8
length = 500
curvecolor = "yellow"

sierpinski_arrowhead_curve(startx,-starty, order, length, curvecolor)

screen.update()
screen.mainloop()
