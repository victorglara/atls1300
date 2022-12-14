""" 
This module requires numpy, opencv and pygame to run. IF you are having issues
with this module, make sure you have the following dependencies (libraries):
    numpy >=
    opencv >=
    pygame >=
"""
import pygame, sys, os
import cv2
import numpy as np
from PIL import Image

class Get():
    def __init__(self, W=480,H=640):
        pygame.init()

        self.W = W #window size
        self.H = H

        self.cam = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop) 
        self.img = self.camImage()
        self.frame = self.img2surf()
        
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.screen = pygame.display.set_mode((W,H))
        self.running = False
        self.selfie()
        
    def selfie(self):
        """Creates pygame instructions and countdown to indicate upcoming capture."""
        #TODO: make a handler
        pygame.display.set_caption("Press any key or CLICK to snap a pic")
        self.running = True
        while self.running:
            self.stream()
    
    def stream(self):
        """Shows a live cast of camera captures for setting up selfie."""
        self.img = self.camImage()
        frame = self.img2surf()
        self.drawFrame(frame)
    
    def camImage(self,color="COLOR"):
        """gets image from camera."""
        # from https://stackoverflow.com/questions/19240422/display-cv2-videocapture-image-inside-pygame-surface
        retval,img=self.cam.read()
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        if color == "BW":
            self.img=cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY)
        # img=np.rot90(img)
        return img
    
    def img2surf(self):
        """Converts cv frame to numpy surface, for drawing and manipulation"""
        frame=pygame.surfarray.make_surface(self.img)
        frame=pygame.transform.rotate(frame,-90)
        return frame
    
    def checkSave(self):
        """prompts text about saving. Needs clock. Is tedious. Dropped."""
        count = 3
        instruct = font.render("Click any key to redo.", True, (0, 0, 0),(255, 255, 255))
        instructRect = instruct.get_rect()
        instructRect.center = (self.W/2, 100)

        self.screen.blit(instruct, instructRect)
        pygame.display.update()

        while count >=0:
            textVal = f"Saving in...{count}"
            text = self.font.render(textVal, True, (255, 255, 255), (0, 0, 0))
            textRect = text.get_rect()
            textRect.center = (self.W/2, self.H-100)

            self.screen.blit(text, textRect)
            pygame.display.update()
            for event in pygame.event.get() :
                if event.type == pygame.KEYDOWN:
                    return False
            pygame.time.wait(1000) 
            count -= 1
        return True
                
    def saveImage(self):
        """save frame (pygame surface) as a gif (using PIL?)"""
        pygame.image.save(self.screen, "tempSelfie.png")
        # convert to gif; from img2gif.py (course code)
        img = Image.open("tempSelfie.png")
        img.convert('RGBA').save("Selfie.gif")#, transparency=transparency) #convert to filetype and save
        os.remove("tempSelfie.png")
        
        # write text on screen, pause and close. Modified from https://www.geeksforgeeks.org/python-display-text-to-pygame-window/        
        text = self.font.render('Saved as Selfie.gif!', True, (255, 255, 255), (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (self.W/2, self.H-100)

        self.screen.blit(text, textRect)
        pygame.display.update()

        pygame.time.wait(3000) #for readability

    def drawFrame(self, frame):
        """Makes a screen and draws an captured image in it."""
        self.screen.blit(frame, (0-self.W/2, 0))
        pygame.display.flip()
        pygame.display.update()
        
        # iterate over the list of Event objects
        # that was returned by pygame.event.get() method.
        for event in pygame.event.get() :
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                self.saveImage()
                #TODO: show image and verify
                    # if KEEP button clicked, close, elif REDO button, continue
                sys.exit() #exit after image
            if event.type == pygame.QUIT:
                self.running=False
                self.cam.release()
            
if __name__ =="__main__":
    Get() #rename takeaselfie?
    