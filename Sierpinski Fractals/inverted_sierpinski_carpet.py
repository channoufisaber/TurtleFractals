# draws an inverted Sierpinski carpet

import turtle

def draw_square(sqx_pos, sqy_pos, sq_length, sq_color, fill_status):
    #setup turtle
    tsq = turtle.Turtle()
    tsq.color(sq_color)
    tsq.penup()
    tsq.setpos(sqx_pos, sqy_pos)
    tsq.pendown()
    tsq.speed(0)
    tsq.hideturtle()

    if fill_status == True:
        tsq.begin_fill()

    #draw square
    for index in range(4):
        tsq.forward(sq_length)
        tsq.right(90)

    if fill_status == True:
        tsq.end_fill()
        
def draw_subordinate_squares(sqx_pos, sqy_pos, sq_length, sq_color, fill_status, nlevel):
    new_size = (1/3) * sq_length
    pos_x = [0, 0, 0, 0, 0, 0, 0, 0]
    pos_y = [0, 0, 0, 0, 0, 0, 0, 0]

    # draw top left square
    pos_x[0] = sqx_pos - (2/3) * sq_length
    pos_y[0] = sqy_pos + (2/3) * sq_length
    draw_square(pos_x[0], pos_y[0], new_size, sq_color, fill_status) 

    # draw the middle left square
    pos_x[1] = sqx_pos - (2/3) * sq_length
    pos_y[1] = sqy_pos - (1/3) * sq_length
    draw_square(pos_x[1], pos_y[1], new_size, sq_color, fill_status) 

    # draw the bottom left square
    pos_x[2] = sqx_pos - (2/3) * sq_length
    pos_y[2] = sqy_pos - (4/3) * sq_length
    draw_square(pos_x[2], pos_y[2], new_size, sq_color, fill_status) 

    # draw the top middle square
    pos_x[3] = sqx_pos + (1/3) * sq_length
    pos_y[3] = sqy_pos + (2/3) * sq_length
    draw_square(pos_x[3], pos_y[3], new_size, sq_color, fill_status) 

    # draw the bottom middle square
    pos_x[4] = sqx_pos + (1/3) * sq_length
    pos_y[4] = sqy_pos - (4/3) * sq_length
    draw_square(pos_x[4], pos_y[4], new_size, sq_color, fill_status) 

    # draw the top right square
    pos_x[5] = sqx_pos + (4/3) * sq_length
    pos_y[5] = sqy_pos + (2/3) * sq_length
    draw_square(pos_x[5], pos_y[5], new_size, sq_color, fill_status) 

    # draw the middle right square
    pos_x[6] = sqx_pos + (4/3) * sq_length
    pos_y[6] = sqy_pos - (1/3) * sq_length
    draw_square(pos_x[6], pos_y[6], new_size, sq_color, fill_status) 

    # draw the bottom right square
    pos_x[7] = sqx_pos + (4/3) * sq_length
    pos_y[7] = sqy_pos - (4/3) * sq_length
    draw_square(pos_x[7], pos_y[7], new_size, sq_color, fill_status)    
    
    if nlevel > 1:
     for i in range(8):
      draw_subordinate_squares(pos_x[i], pos_y[i],new_size, sq_color,fill_status, nlevel - 1)

def draw_sierpinski_carpet(qx_pos, qy_pos, sq_length, sq_color, fill_status, nlevel):
   if nlevel <= 0:
      return
   elif nlevel == 1:
      draw_square(qx_pos, qy_pos, sq_length, sq_color, fill_status)
   elif nlevel >= 1:
      draw_square(qx_pos, qy_pos, sq_length, sq_color, fill_status)
      draw_subordinate_squares(qx_pos, qy_pos, sq_length, sq_color, fill_status, nlevel-1)
       
       
  
screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor(0, 0, 0)
screen.delay(0)
screen.tracer(0)

# change these parameters for different results
sq_color = "blue"
sq_size = 200
sq_x = -100
sq_y = 100
level = 5

draw_sierpinski_carpet(sq_x, sq_y, sq_size, sq_color, True, level)

screen.update()
screen.mainloop()