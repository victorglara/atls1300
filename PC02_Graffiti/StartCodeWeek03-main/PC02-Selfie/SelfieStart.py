"""
SELFIE starter code
ATLS 1300/5650
Author: Dr. Z
Author: YOUR NAME
DATE

DESCRIPTION:
By choosing this start code, you are choosing to use a selfie as your background 
for drawing. The selfie code will run automatically.

A screen will open with instructions on the window label. The snapshot will 
automatically be used as the background. The selfie library is bare bones--there 
is no countdown. 
    To retake an image, simply run your code again. 
    To keep an image, comment out the line 31 (instructions in comments), 
    and run the code again.

The code will CONTINUE TO RUN (meaning you cannot run it again) when you close 
the window! You must make sure all images you reference in the code is in the same folder as this script!

"""
#==============================IMPORT LIBRARIES===============================
import turtle
import selfie

#==============================================================================
#==============================SETUP TURTLE WINDOW===============================
win = turtle.Screen()
W = 480 # change this value to change your window width 
H = 640 # change this value to change your window height 
win.setup(width=W, height=H)

#============================== SET UP BACKGROUND ===============================
# selfie.Get() # take a selfie! (Note, may be slow)
# comment the line above to work with the last the selfie you took!

# add image to background
selfImg = "Selfie.gif" # name of the selfie file. DO NOT CHANGE.
win.addshape(selfImg)
win.bgcolor("black") # sets background to black. Type in strings to change color
win.bgpic(selfImg) # adds image on top of background.

#============================== DRAW WITH TURTLES ===============================
t = turtle.Turtle("circle") # starts with circle shape

# you can use the entire selfie image as a stamp by setting the turtle shape to selfImg
#turtle.shape(selfImg)

t.forward(100)
t.right(90)
t.forward(100)

#============================== CLEAN UP ===============================
# This line below is needed to keep loops running so that window stays open. 
# Code stops running when window is closed.
turtle.done()
