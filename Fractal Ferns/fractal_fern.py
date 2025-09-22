# Algorithm Credit: https://en.wikipedia.org/wiki/Barnsley_fern
# Fern Parameters Credit: https://www.chradams.co.uk/fern/maker.html

import turtle
import random
import time

def draw_fractal_fern(a, b, c, d, e, f, p, max_interations, pen, scale_x, scale_y, offset_x, offset_y):
    x, y = 0, 0
    xn, yn = 0, 0

    for n in range(max_interations):
        pen.goto( scale_x * xn - offset_x, scale_y * yn - offset_y)
        pen.pendown()
        pen.dot(3)
        pen.penup()
        r = random.random()
        if r < p[0]:
            xn =  a[0] * x + b[0] * y + e[0]
            yn =  c[0] * x + d[0] * y + f[0]
        elif r < p[0] + p[1]:
            xn =  a[1] * x + b[1] * y + e[1]
            yn =  c[1] * x + d[1] * y + f[1]
        elif r < p[0]+ p[1] + p[2]:
            xn =  a[2] * x + b[2] * y + e[2]
            yn =  c[2] * x + d[2] * y + f[2]
        else:
            xn =  a[3] * x + b[3] * y + e[3]
            yn =  c[3] * x + d[3] * y + f[3]
        x = xn
        y = yn

def print_time_stats(start_time, end_time, max_interations):
    time_elapsed = end_time - start_time
    hrs = int(time_elapsed / 3600)
    mins = int(time_elapsed / 60)
    secs = int(time_elapsed % 60)
    print(f"Plot time - {fern_name}:", '{:02d}:{:02d}:{:02d}'.format(hrs, mins, secs))
    print(f"Iterations: {max_interations}")


# Uncomment fern and offset parameters to plot desired fern

## Barnsley fern parameters
fern_name = "Barnsley"

a = [0.0, 0.85, 0.20, -0.15]
b = [0.0, 0.04, -0.26, 0.28]
c = [0.0, -0.04, 0.23, 0.26]
d = [0.16, 0.85, 0.22, 0.24]
e = [0.0, 0.0, 0.0, 0.0]
f = [0.0, 1.60, 1.60, 0.44]
p = [0.01, 0.85, 0.07, 0.07]
## Offsets for positioning Barnsley fern
offset_x = 25
offset_y = 190
##

## Modified Barnsley fern parameters
""" fern_name = "Modified Barnsley"

a = [0.0, 0.845, 0.20, -0.15]
b = [0.0, 0.035, -0.31, 0.24]
c = [0.0, -0.035, 0.255, 0.25]
d = [0.20, 0.82, 0.245, 0.20]
e = [0.0, 0.0, 0.0, 0.0]
f = [-0.12, 1.60, 0.29, 0.68]
p = [0.01, 0.85, 0.07, 0.07] """
## Offsets for positioning modified Barnsley fern
""" offset_x = 25
offset_y = 150 """
##

## Cyclosorus fern parameters
""" fern_name = "Cyclosorus"

a = [0.0, 0.95, 0.035, -0.04]
b = [0.0, 0.005, -0.20, 0.20]
c = [0.0, -0.005, 0.16, 0.16]
d = [0.25, 0.93, 0.04, 0.04]
e = [0.0, -0.002, -0.09, 0.083]
f = [-0.4, 0.5, 0.02, 0.12]
p = [0.02, 0.84, 0.07, 0.07] """
## Offsets for positioning Cyclosorus fern
""" offset_x = 25
offset_y = 120 """
##

## Culcita fern parameters
""" fern_name = "Culcita"

a = [0.0, 0.85, 0.09, -0.09]
b = [0.0, 0.02, -0.28, 0.28]
c = [0.0, -0.02, 0.30, 0.30]
d = [0.25, 0.83, 0.11, 0.09]
e = [0.0, 0.0, 0.0, 0.0]
f = [-0.14, 1.0, 0.60, 0.70]
p = [0.02, 0.84, 0.07, 0.07] """
## Offsets for positioning Culcita fern
""" offset_x = 25
offset_y = 120 """
##


## scale parameters for fitting fern inside the window
scale_x = 65
scale_y = 37
scalefactor = 2

fscale_x = scale_x * scalefactor 
fscale_y = scale_y * scalefactor
foffset_x = offset_x * scalefactor
foffset_y = offset_y * scalefactor

## change this to increase or decrease level of detail
max_interations = 10000

screen = turtle.Screen()
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.color("orange")
pen.penup()

start_time = time.time()

draw_fractal_fern(a, b, c, d, e, f, p, max_interations,pen, fscale_x, fscale_y, foffset_x, foffset_y)
screen.update()

end_time = time.time()

print_time_stats(start_time, end_time, max_interations)

screen.mainloop()