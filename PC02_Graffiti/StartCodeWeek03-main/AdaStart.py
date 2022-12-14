'''
Turtle starter code
ATLS 1300
Author: Dr. Z

Author: YOUR NAME
DATE

DESCRIPTION:
By choosing this start code, you are choosing to use a Ada Lovelace as your background 
for drawing. 

You must make sure all images you reference in the code is in the same folder as this script!
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)
turtle.speed(0)

# Create a panel to draw on. 
win = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
win.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Ada's image to it
win.bgcolor("seashell4")
bgImg = "FullAda_Glam.gif"
stampImg = "algorithm.gif"
adaStamp = "JustAda_Glam.gif"
win.addshape(adaStamp)
win.addshape(stampImg) # Now you can use Ada's image as a stamp. USE THE DOCS.



win.bgpic(bgImg) # sets the background to the selected image.
#Comment out the line above to remove the image from background

algo = turtle.Turtle()
algo.speed(0)
algo.ht()
algo.penup()
algo.shape(stampImg)
algo.shapesize(5,5,12)
algo.goto(300,300)
algo.stamp()
algo.goto(200,200)
algo.stamp()
algo.shape(stampImg)
algo.goto(-100,-100)
algo.stamp()
algo.goto(-150,-150)
algo.stamp()

justAda = turtle.Turtle()
justAda.ht()
justAda.speed(0)
justAda.penup()
justAda.shape(adaStamp)
justAda.stamp()

square1 = turtle.Turtle()
square1.speed(10)
square1.ht()
square1.penup()
square1.color('cyan')
square1.pensize(15)
square1.goto(-275,400)
square1.right(45)
square1.pendown()
square1.forward(750)
square1.right(90)
square1.forward(500)
square1.right(90)
square1.forward(750)
square1.right(90)
square1.forward(500)

justAda.goto(150,150)
justAda.stamp()

triang = turtle.Turtle()
triang.ht()
triang.color('magenta')
triang.pensize(8)
triang.penup()
triang.goto(300,-300)
triang.left(120)
triang.pendown()
triang.forward(300)
triang.left(120)
triang.forward(300)
triang.left(120)
triang.forward(300)

justAda.goto(-150,-150)
justAda.stamp()

hex = turtle.Turtle()
hex.ht()
hex.color('yellow')
hex.penup()
hex.goto(-300, 300)
hex.pensize(10)
hex.pendown()

for i in range(6):
    hex.forward(200)
    hex.left(300)

#=======Add your code here======



#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
turtle.done()