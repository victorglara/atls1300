'''
Turtle starter code
ATLS 1300/5650
Author: Dr. Z

Author: YOUR NAME
DATE

This is a description of what this code does. You should edit this line to get full credit on assignments.
The code will CONTINUE TO RUN (meaning you cannot run it again) when you close the window!
'''

import turtle # import the library of commands that you'd like to use
turtle.colormode(255) # so you can use standar RGB values, 0-255

#Create a panel to draw on. 
win = turtle.Screen()
w = 700 # width of panel
h = 700 # height of panel
win.setup(width=w, height=h) #700 x 700 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

#====================================================== Your code ======================================================

palette = ["blue", "red", "orange", "purple"]
#great to have these all in one place. now how do we get acces into a specific one?
#this is called indexing, where blue is 0, red is 1, orange is 2, and purple is 3
print(palette[0])

#lists are indicated with square brackets around balues
#syntax: [value, value value ]
#accepts any data type: strings, integers, booleansd
#can you mix integers and strings? 


#tuple
#indicated by parantheses around value
#synatx (value, value, value)
#you cannot overwrite tuple values
#accepts any data type: strings, integers, booleans even other tuples
#separate values with commas
#someTuple = ("red", "green", "blue")

positions = ((0,0), (0,100), (100,100), (100,0))
#this is a tuple of tuples
#this tuple has 4 values saved to them
print(positions[0])
#to access first value:
print(positions[0][0])

# Indexing: how we can access data in our lists
#lists and tuples are pill boxes
#the "box" is made up of leablerd elements, that store values (values can be anything: str, int, bool)
#instead of days of the week, they are labeled with numbers. starting at 0. 
#index (singular), indices(plural)
#starting at 0

print(palette[0])
print(positions[3][0])

print(positions[-1])#print last element

square = turtle.Turtle()
square.ht()
square.speed(10)
square.pensize(20)

for elem in palette: #for each element in the variable positions, complete a task
    #elemt is an iterator variable, iterating through all the values stored in the platte list
    square.pencolor(elem)
    print(elem) #there are 4 elements, so it will print 'repeat' 4 times
    square.forward(100)
    square.right(90)
   

#======= Clean up, required to run properly ======
turtle.done() # nothing should come after this line of code!
