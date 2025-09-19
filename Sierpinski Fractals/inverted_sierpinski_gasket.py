# draws inverted sierpinski gasket

import turtle
import math

def draw_eqilateral_triangle(tr_pos_x, tr_pos_y, tr_size, tr_color):
    t1 = turtle.Turtle()
    drw_angle = 120

    t1.color(tr_color)
    t1.penup()
    t1.setpos(tr_pos_x,tr_pos_y)
    t1.pendown()
    t1.hideturtle()

    t1.forward(tr_size)
    t1.left(drw_angle)
    t1.forward(tr_size)
    t1.left(drw_angle)
    t1.forward(tr_size)
    
# draws inverted triangle (tr_pos_x, tr_pos_y) = location of the vertex
def draw_dividing_triangle(tr_pos_x, tr_pos_y, tr_size, tr_color):
    t1 = turtle.Turtle()
    drw_angle = 120

    t1.color(tr_color)
    t1.penup()
    t1.setpos(tr_pos_x,tr_pos_y)
    t1.pendown()
    t1.hideturtle()

    t1.begin_fill()
    t1.left(drw_angle)
    t1.forward(tr_size)
    t1.right(drw_angle)
    t1.forward(tr_size)
    t1.right(drw_angle)
    t1.forward(tr_size)
    t1.end_fill()

# draws the three smaller triangles which surround the "mother" triangle
def draw_subordinate_triangles(tr_pos_x, tr_pos_y, tr_size, tr_color, nlevel):
    ang_radians = math.radians(30)
    new_size = 0.5 * tr_size

    # draw top triangle
    x_pos1 = tr_pos_x
    y_pos1 = (tr_size * math.cos(ang_radians)) + tr_pos_y
    draw_dividing_triangle(x_pos1, y_pos1, new_size, tr_color)
   
    # draw bottom left triangle
    x_pos2 = tr_pos_x - new_size
    y_pos2 = tr_pos_y
    draw_dividing_triangle(x_pos2, y_pos2, new_size, tr_color)

    # draw bottom right triangle
    x_pos3 = tr_pos_x + new_size
    y_pos3 = tr_pos_y
    draw_dividing_triangle(x_pos3, y_pos3, new_size, tr_color)
   
    # recurse for specified number of levels
    if nlevel > 1:
        draw_subordinate_triangles(x_pos1, y_pos1, new_size, tr_color, nlevel - 1)
        draw_subordinate_triangles(x_pos2, y_pos2, new_size, tr_color, nlevel - 1)
        draw_subordinate_triangles(x_pos3, y_pos3, new_size, tr_color, nlevel - 1)

def draw_sierpinski_triangle(startx, starty, tr_pos_x, tr_pos_y, tr_size, tr_color, nlevel):
    if nlevel < 0:
        return
    else:
        draw_eqilateral_triangle(startx, starty, tr_size, tr_color)

        if nlevel == 0:
            return
        if nlevel == 1:    
            draw_dividing_triangle(tr_pos_x, tr_pos_y, tr_size / 2, tr_color)
            return
        elif nlevel > 1:
            draw_dividing_triangle(tr_pos_x, tr_pos_y, tr_size / 2, tr_color)
            draw_subordinate_triangles(tr_pos_x, tr_pos_y, tr_size / 2, tr_color, nlevel - 1)

screen = turtle.Screen()
screen.setup(1600, 1000)
screen.bgcolor(0,0,0)
screen.delay(0)
screen.tracer(0)

# change these parameters for different results
startx = -400
starty = -400
tsize = 800
tx = startx + (tsize / 2)
ty = starty
tcolor = "red" 
tlevel = 3

draw_sierpinski_triangle(startx, starty, tx, ty, tsize, tcolor, tlevel)

screen.update()
screen.mainloop()
