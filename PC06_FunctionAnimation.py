# Victor G. Lara 
#ATLS1300 - PC06 Animating with Functions 
''' This script shows a concentric circle pattern that animates with a number of different colors on the screen'''

import math, random
import pygame
pygame.init()


#create window

w = 750
h = 750
win = pygame.display.set_mode((w,h))
pygame.display.set_caption("PC06 Animating Functions - Victor Lara")
win.fill((0,0,0))

clock = pygame.time.Clock() #create a clock object, a function that can remember its own data = object


#   DEFINE FUNCTIONS
def circ(win, color, x, y):
    '''This function creates a circle, the last argument width is usually 0, 
    which yields a filled circle, but in this case we use width=4 to get a circle
    with an empty fill to get the concentric circle pattern'''
    pygame.draw.circle(win, color,(x,y), rad, width=4)


def limits():
    '''The function limits() defines the minimum radius of the circle 5, and the maximum radius which is 200
    Additionally, this funciton also sets the State of the animation to 0 which implies a particular 
    order of colorIndex to print a different order in the printing of the color in the concentric circle animation'''
    global rad 
    global inc
    global colorIndex
    global State
    if rad >= 350: #sets radius limit to 350
        inc *= -1
        if(State==0) : #if the animation State is 0, the animation traverses through the colors of the palette by adding one to the list index
            colorIndex=colorIndex+1
        
        circ(win, (255,255,255),x,y) #circle prints white in order to indicate that it has reached its max radius
    if rad <= 5 :
        inc *= -1
        circ(win, (255,255,255),x,y) #when the radius is at its minimum, 5, it also prints in white to indicate minimum
       
        if(State==0): #when State = 0, the program prints the entire concentric pattern in a single color each time it prints the pattern
            colorIndex=colorIndex+1
            
    if colorIndex >= len(palette) and State==0: #this condition sets the colorIndex to 0 if it reaches the maximum amount of values in the list palette, so when the function is run in a while (infinite) loop, the program can traverse the color list palette forever
        colorIndex = 0


# color palette for the circles 
palette = [(0, 18, 25),(0, 95, 115),(10, 147, 150),(148, 210, 189),(233, 216, 166),
            (238, 155, 0),(202, 103, 2),(187, 62, 3),(174, 32, 18),(155, 34, 38)]

#global variables used throughout
x = w/2
y = h/2
rad = 5
inc = 10
running = True
State=0
colorIndex=0
i=0

while running:
    circ(win, (palette[colorIndex]),x, y) #display circle from function, animates continously
    rad += inc #adds inc, increasing value of radius by 10
    limits() #calls the limits function to set radius boundaries, and limits radius min and max

    if(State==1): #if State is 1, the program travels throught the color palette in a single print of the pattern by changing the color of each circle in order by adding one to indexing value
        i=i+1
        colorIndex=i%len(palette) #use modulo to get values within the length of palette, can only increase up to 9, which is the amount of RGB values in the list palette
    if(State==2): # State 2 changes the animation so that it chooses colors in the concentric circle pattern randomly
        colorIndex = random.randint(-1,(len(palette)-1))
   
    pygame.display.update()

    clock.tick(20) # set fps, animation appearance speed

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False # stops animation

pygame.quit()