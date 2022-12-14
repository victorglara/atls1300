"""
@author: sazamore

This script will help you learn how to debug 
your code, or someone else's! Run the code and read the error report
and try to find the error. 

Each fixed bug is 1 extra credit MiniProject point.
To complete the task:
    1. For every bug you fix, add the following comment at the end of 
    the line # debugged <ERRORTYPE>
    Possible ERRORTYPEs:
        IndentError
        IndexError
        NameError
        SyntaxError
        TypeError
    2. If you get all 5, make sure the final image looks 
    like the one in the assignment
 
                There are 5 bugs in this code. 
            New coding concepts will not have bugs.
             *** 1 bug will not throw a error! ***
   
Later, we'll use the code to investigate how to work with if statements and for loops.
You may use parts of code in your programming challenges, but please
cite it ("Borrowed/modified from Dr. Z's code.")
"""
import turtle, random


# ================ set up ======================
turtle.colormode(255) # accept RGB color values between 0 and 255
turtle.tracer(0) # turn off turtle animation 

# Create a window to draw on. 
win = turtle.Screen()
w = 750 # width of win
h = 750 # height of win
win.setup(width=w, height=h) 

# ================ define variables =============
queenBlue = (87, 117, 144)

maizeCrayola = (243, 202, 64)
yellowOrange = (242, 165, 65)
mangoTango = (240, 138, 75)
middleRed = (215, 138, 118)
# colors from coolors.co 

# choose colors to work with (changes each time the script is run)
color1 = random.choice((maizeCrayola,yellowOrange,mangoTango, middleRed))
color2 = random.choice((maizeCrayola,yellowOrange,mangoTango, middleRed))
color3 = random.choice((maizeCrayola,yellowOrange,mangoTango, middleRed))    

squiggles = turtle.Turtle(visible=False) # make a turtle invisible from the start!

# ================== do tasks ===================

win.bgcolor(queenBlue) # set background color #debugged <NameError>
squiggles.color(color1) # set the first color of the line
squiggles.width(6) # lets make it thicc

# draw squiggles
for i in range(500):
    # this for loop repeats the indentd lins below 500 times, 
    # We'll learn about for loops in Week 5!

    squiggles.forward(random.randint(4,9)) #move forward some random amount
    squiggles.left(random.randint(-70,70)) #debugged <IndentError>
    
    # get x position of the turtle
    pos = squiggles.xcor() # this is a tuple: (x,y)
    if pos < -200:
        # on the left side of the screen, choose color 2
        squiggles.color(color2)
    elif -200 <= pos < -200:
        # in the middle of the screen, choose color 3
        squiggles.color(color3)
    else: 
        pos == pos #debugged <SyntaxError>
        # otherwise, back to color 1
        squiggles.color(color1)

turtle.update() # manual window update, since turtle animation off        
turtle.done()
