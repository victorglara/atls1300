'''
Turtle starter code
ATLS 1300/5650
Author: Dr. Z

Author: Victor G. Lara

This script runs a turtle animation inspired by Wassily Kandisnky's 'Circles in a Circle'
composition. 
'''

import turtle # import the library of commands that you'd like to use
turtle.colormode(255) # so you can use standar RGB values, 0-255

#Create a panel to draw on. 
win = turtle.Screen()
w = 1500 # width of panel
h = 1500 # height of panel
win.setup(width=w, height=h) #700 x 700 is a decent size to work on. 
win.bgcolor(236, 226, 208)
#You can experiment by making it the size of your screen or super tiny!

#====================================================== Your code ======================================================

stripe0 = turtle.Turtle()
stripe0.ht()
stripe0.speed(8)
stripe0.pensize(2)
stripe0.goto(160, 520)
stripe0.up()


bigCircle = turtle.Turtle()
bigCircle.speed(8)
bigCircle.pensize(40)
bigCircle.ht()
bigCircle.up()
bigCircle.right(90)
bigCircle.forward(450)
bigCircle.left(90)
bigCircle.down()
bigCircle.circle(450)

stripe0.pensize(4)
# stripe0.down() #put pen down
stripe0.goto(560,-250)
stripe0.down()
stripe0.goto(-350, -222)

circle = turtle.Turtle()
circle.speed(8)
circle.pensize(5)
circle.shape("circle")
circle.hideturtle()
circle.color("black","#FC8D23")
circle.begin_fill()
circle.circle(100) #draw a circle
circle.end_fill()
circle.up() #pick up pen
circle.goto(130, 150)
circle.down() #put pen down
circle.color("black","#037881")
circle.begin_fill()
circle.circle(100) #draw a circle
circle.end_fill()
circle.up()
circle.goto(-139,140)
circle.down()
circle.color("black","#064F1B")
circle.begin_fill()
circle.circle(100)
circle.end_fill()
circle.up()
circle.goto(-139,-140)
circle.down()
circle.color("black","#FB701C")
circle.begin_fill()
circle.circle(100)
circle.end_fill()
circle.up() #pick up pen
circle.goto(130, -150)
circle.down() #put pen down
circle.color("black","#AC0000")
circle.begin_fill()
circle.circle(100) #draw a circle
circle.end_fill()


stripe = turtle.Turtle()
stripe.ht()
stripe.shape("circle")
stripe.pensize(10)
stripe.up() #pick up pen
stripe.goto(130, 150)
stripe.pensize(6)
stripe.down() #put pen down
stripe.goto(460,-250)
stripe.up()
stripe.goto(-600, -200)
stripe.down()
stripe.pensize(8)
stripe.goto(200, 250)
stripe.up() #pick up pen
stripe.goto(230, 250)
stripe.down() #put pen down
stripe.pensize(5)
stripe.goto(-500, -400)
stripe.down()
#======= Clean up, required to run properly ======
turtle.done() # nothing should come after this line of code!