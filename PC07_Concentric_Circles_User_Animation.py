# Victor G. Lara 
#ATLS1300 - PC06 Animating with Functions 
''' This script shows a concentric circle pattern that 
animates with a number of different colors on the screen.
Additionally, there are key controls to change the state of 
the animation'''

#IMPORT LIBRARIES   
import random
import pygame
import this
pygame.init()


#   CREATE WINDOW   
w = 750
h = 750
win = pygame.display.set_mode((w,h))
pygame.display.set_caption("PC07 Interactive Animation - Victor Lara")
clock = pygame.time.Clock() #create a clock object, a function that can remember its own data = object
rad = 5
inc = 10


#   DEFINE FUNCTIONS
def circ(win, color, x, y):
    '''This function creates a circle, the last argument width is usually 0, 
    which yields a filled circle, but in this case we use width=4 to get a circle
    with an empty fill to get the concentric circle pattern'''
    pygame.draw.circle(win, color,(x,y), rad, width=4)

def limits(x,y):
    '''The function limits() defines the minimum radius of the circle 5, and the maximum radius which is 200
    Additionally, this funciton also sets the State of the animation to 0 which implies a particular 
    order of colorIndex to print a different order in the printing of the color in the concentric circle animation.
    Requires x and y position arguments'''
    global inc
    global colorIndex
    if rad >= 350 :
        inc *= -1
        if(State==0) :
            colorIndex=colorIndex+1
        
        circ(win, (255,255,255),x,y)  
    if rad <= 5 :
        inc *= -1
        circ(win, (255,255,255),x,y) 
       
        if(State==0) :
            colorIndex=colorIndex+1
            
    if colorIndex >= len(palette) and State==0:
        colorIndex = 0

def changeState():
    '''This functions adds a value to the variable State,
    which in turn changed the mode of the function.
    The conditional is set to limit the additon 3, after that
    State resets to 0, returning to its original state'''
    global State
    State = State + 1
    if State >= 3:
        State = 0

def printMouse():
    '''This function gets the position of the mouse.
    It is used to provide x,y values for interactivity, 
    allowing users to change the center, or position of 
    concentric circle animation'''
    return pygame.mouse.get_pos()

#   ANIMATION LOOP SETUP
'''The two palettes in the bottom are used to print 
the colors of the circle pattern, and to change the 
background colors as users change animation State/mode'''
palette = [(0, 18, 25),(0, 95, 115),(10, 147, 150),(148, 210, 189),(233, 216, 166),
            (238, 155, 0),(202, 103, 2),(187, 62, 3),(174, 32, 18),(155, 34, 38)]

winpalette = [(13, 13, 13), (68, 68, 68),(106, 106, 106),(189, 189, 189),(189, 189, 189),
            (215, 215, 215), (162, 162, 162), (121, 121, 121), (92, 92, 92),(72, 72, 72), 
            (70, 70, 70)] #greyscale


rad = 5
inc = 10
running = True
State=0
colorIndex=0
i=0

def main():
    '''Main function will run most of the code, then it can all be called in a single line. '''
    x = w/2
    y = h/2
    global running
    global colorIndex
    global rad

    global i
    while running:
        #main while loop shows continous animation
        circ(win, (palette[colorIndex]),x, y)#display circle from function, animates continously
        rad += inc #adds inc, increasing value of radius by 10
        limits(x,y) #calls the limits function to set radius boundaries, now requires to arguments 

        if(State==1): #if State is 1, the program travels throught the color palette in a single print of the pattern by changing the color of each circle in order by adding one to indexing value
            i=i+1
            colorIndex=i%len(palette) #use modulo to get values within the length of palette, can only increase up to 9, which is the amount of RGB values in the list palette
        if(State==2):# State 2 changes the animation so that it chooses colors in the concentric circle pattern randomly
            colorIndex = random.randint(-1,(len(palette)-1))
    
        pygame.display.update()

        clock.tick(20) # set fps, animation appearance speed


        '''Add key interactions here for user interactivity'''
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False # stops animation
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed(): #if mouse gets pressed
                        '''When mouse gets pressed, the pogram returns mouse location values, 
                        these values are used to print the animation again at the moust position
                        where it was clicked, the program also changes State each time users click.'''
                        mousePos = printMouse()
                        x = mousePos[0] #gets x position from mouse click
                        y = mousePos[1] #gets y position from moouse click
                        changeState() #each time a user clicks, it also changes animation State
                        circ(win, (palette[colorIndex]),x, y) #shows animation now using user click position

                if pygame.key.get_pressed()[pygame.K_SPACE]:
                    '''if user presses space bar, runs the changeState
                    function changing the animation mode, and in this key
                    there is also a random change in the backgound color'''
                    changeState()
                    win.fill(random.choice(winpalette))

                if pygame.key.get_pressed()[pygame.K_BACKSPACE]:
                    '''if user presses backspace key, runs the changeState
                    function changing the animation mode'''
                    changeState()

                # if pygame.key.get_pressed()[pygame.K_BACKSPACE]:
                    '''this remains a work in progress attempting to get a 
                     jpg file that shows a screenshot or still image from 
                    user's unique animation'''
                #     pygame.image.save(win, "screenshot.jpg")
                    #need extra code if you want to save a file and make a new one, instead of overwriting the same one

        pygame.display.update()

main()
pygame.quit()