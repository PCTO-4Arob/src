'''
Start menu

https://github.com/PCTO-OneTwoCode
'''

#import libraries
import pygame, sys, time
from pygame.locals import *
import random

#pygame initialization
pygame.init()


#----------------------------------------
# CLASSES
#----------------------------------------


#This class contains the background method
class Background():
    #constructor
    def __init__(self, x, y, filepath='./sprites/background.jpg'):
        try:
            #load the image
            self.image = pygame.image.load(filepath)
            self.rect = self.image.get_rect()
            self.rect = self.rect.move(0,0)
            #resize it using the screen sizes
            self.fullScreenImage = pygame.transform.scale(self.image, (x,y))
            
        except Exception as e:
            #print the exception on the screen
            print('error: ', str(e))

    #update the background status
    def update(self):
        self.rect.move(self.rect.center[0]+5,self.rect.center[1])
        screen.blit(self.fullScreenImage, self.rect)


#this class contain the title displayed on the screen
class Title():
    #constructor
    def __init__(self, x, y, filepath='./sprites/title.png'):
        try:
            #load the image and move it to the right position
            self.image = pygame.image.load(filepath)
            self.rect = self.image.get_rect()
            self.rect = self.rect.move(x, y)
            #self.image = pygame.transform.scale(image,(50,50))
        except Exception as e:
            #print the error on the screen
            print('error: ', str(e))

    #this method update the title status
    def update(self):
        screen.blit(self.image, self.rect)


#this class has been made to control buttons
class Button():
    #constructor
    def __init__(self, filepath, screen_width, screen_height):
        self.screen_height = screen_height
        self.screen_width = screen_width

        try:
            #load the image
            self.image = pygame.image.load(filepath)
            self.rect = self.image.get_rect()
            self.rect = self.rect.move(0,self.screen_height)
        except Exception as e:
            #print the error on the screen
            print('error: ', str(e))

    #return the y cordinate of the button        
    def getY(self):
        return self.rect.center[1]

    #update the button status
    def update(self,x,y):
        #controls if the user press the button
        if self.rect.collidepoint(x, y):
            return True
        screen.blit(self.image, self.rect)

    #change the image of the button if it is the volume button
    def changeStatus(self, imgName, x, y, soundTrack, silent):
        #if the buttom is pressed change the button status
        if self.rect.collidepoint(x, y):
            #load the button click sound
            soundEffect = pygame.mixer.Sound("./btnClick.wav")
            pygame.mixer.Sound.set_volume(soundEffect,0.5)#0.5 is the volume
            pygame.mixer.Sound.play(soundEffect,0) #play the track
            
            try:
                #load a new button image
                self.image = pygame.image.load(imgName)
                self.rect = self.image.get_rect()
                self.rect = self.rect.move(0,self.screen_height)
                #if the volume is on, it turns it off
                if not silent:
                    pygame.mixer.Sound.set_volume(soundTrack,0.0)#0.0 is the volume
                else: #else it turn it on
                    pygame.mixer.Sound.set_volume(soundTrack,0.5)#0.5 is the volume
                
            except Exception as e:
                #print the exception on the screen
                print('error: ', str(e))

        screen.blit(self.image, self.rect)
        

#this class manage the hay on the screen
class Hay(pygame.sprite.Sprite):
    #constructor
    def __init__(self, pos, filepath='./sprites/hayl.png'):
        #initialize a new sprite
        pygame.sprite.Sprite.__init__(self)
        self.pos = pos
        #load the sprite image
        self.image = pygame.image.load(filepath)
        self.rect = self.image.get_rect()

        self.rect = self.rect.move(self.pos)
        #set the speed to -1, because the sprite moves from right to left
        self.speed = -1

    #this method update the sprite status
    def update(self, time, width):
        #if the time is odd, it moves the sprite
        if time%2 == 0:
            self.rect = self.rect.move([self.speed,0])
            if self.rect.center[0] <= 0: #if the sprite reaches the end of the screen it returns true
                return True
        screen.blit(self.image, self.rect)



#-------------------------
# FUNCTIONS
#-------------------------

#this function control if it is the case to quit the game
def controlExit(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()


#this is the main function
def menu():

    #screen is the display
    global screen 
    width, height = 1000,600 #screens size
    screen = pygame.display.set_mode((width,height))
    

    #initialize objects
    background = Background(width, height)
    title = Title(width//6 * 5, height//6*5)
    hay = Hay((width,450))
    
    #initialize sound track
    soundTrack = pygame.mixer.Sound("./startMenu.wav")
    pygame.mixer.Sound.set_volume(soundTrack,0.5)#0.5 is the volume
    pygame.mixer.Sound.play(soundTrack,-1)#the -1 let the sound repeates when it ends
    silent = False #this variables control if the screen is muted

    #this dictionary cointains all of the buttons 
    buttonList = {}

    btnPlay = Button('./sprites/btnplay.png', width, height//4)
    btnExit = Button('./sprites/btnexit.png', width, btnPlay.getY() + 100)
    btnMode = Button('./sprites/volume.png', width, btnExit.getY() + 100)
    buttonList[1] = btnPlay 
    buttonList[0] = btnExit
    buttonList[2] = btnMode
    
    #time count how many cicles the program perform
    time = 0

    #this while loop control the screen animations
    while True:

        #updates elements
        background.update()
        title.update()
        if hay.update(time, width):
            hay = Hay((width,450))  
        btnPlay.update(width, height)
        btnExit.update(width, height)
        btnMode.update(width, height)
        
        
        for event in pygame.event.get():
            controlExit(event)

            #if the mouse is pressed it control if it is the case
            #to change the buttons status
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                for key, value in buttonList.items():
                    x, y = event.pos
                    
                    if key == 2:
                        if silent:
                            btnMode.changeStatus('./sprites/volume.png', x, y, soundTrack, silent)
                        else:
                            btnMode.changeStatus('./sprites/mute.png', x, y, soundTrack, silent)
                        silent = not silent
                    elif value.update(x, y) == True: 
                        return key

        #update screen status
        pygame.display.update()
        time += 1
    

if __name__ == "__main__":
    menu()
