'''
Victor Lara
PC04 Parametric Art

This script runs a turtle animation that draws a concentric circle pattern/stamp
and then loops through the same stamp a few times while iterating through 
a color list, as well as x-offset increments. 
'''
import math, random, time
from secrets import choice
import turtle

turtle.tracer(0) # turns off turtle animation

#window set up
win =turtle.Screen()
w = 700 # width of panel
h = 700 # height of panel
win.setup(width=w, height=h) 
win.bgcolor((0,0,0))


#variable definition
numCirc = turtle.Turtle()
palette = ["#0aefff","#147df5"]
palette1 = ["#ff0000","#ff8700","#ffd300","#deff0a","#a1ff0a","#0aff99","#0aefff","#147df5","#580aff","#be0aff"]
x_offset = 1
rad = 1
inc = 10
number = random.randint(0,360)
colors = len(palette)

numCirc.penup()
numCirc.pensize(4.5)

for p in range(15):
    # repeats concentric circle pattern
    centerx = 50*p # center of pattern, horizontal
    centery = 0*p # center of patter, vertical
    numCirc.goto(centerx,centery)
    rad = 15 # reset radius
    print(p)
    numCirc.color(choice(palette1))
    for i in range(25):
        # draw concentric circles, based on number of colors
        # change color here to change color of entire pattern 
        # numCirc.color(palette[i])
        for t in range(360):
            # draws a single circle
            # t = math.radians(i)
            x = rad * math.cos(math.radians(t))
            y = rad * math.sin(math.radians(t))
            numCirc.goto(x+centerx,y+centery) # added to the turtle position
            numCirc.down() # starts drawing circle at first point
        numCirc.penup()
        rad += inc

    turtle.update()


turtle.done()