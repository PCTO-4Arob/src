'''
Start menu

https://github.com/PCTO-OneTwoCode
'''

#import libraries
import pygame, sys, time
from pygame.locals import *
import random
import os
import speech_recognition as sr

pathname = os.path.dirname(os.path.realpath(__file__))

#pygame initialization
pygame.init()
pygame.mixer.init()

recognizer = sr.Recognizer()


#----------------------------------------
# CLASSES
#----------------------------------------


#This class contains the background method
class Background():
    #constructor
    def __init__(self, x, y, filepath=os.path.join(pathname, 'sprites/background.jpg')):
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
    def update(self,screen):
        self.rect.move(self.rect.center[0]+5,self.rect.center[1])
        screen.blit(self.fullScreenImage, self.rect)


#this class contain the title displayed on the screen
class Title():
    #constructor
    def __init__(self, x, y, filepath=os.path.join(pathname, 'sprites/title.png')):
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
    def update(self,screen):
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
    def update(self,screen,x,y):
        #controls if the user press the button
        if self.rect.collidepoint(x, y):
            return True
        screen.blit(self.image, self.rect)

    #change the image of the button if it is the volume button
    def changeStatus(self, imgName, x, y, soundTrack, silent):
        #if the buttom is pressed change the button status
        if self.rect.collidepoint(x, y):
            #load the button click sound
            soundEffect = pygame.mixer.Sound(os.path.join(pathname, "btnClick.wav"))
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
    
    def changeStatusTo(self,screen, filepath, soundTrack, silent):
        
        soundEffect = pygame.mixer.Sound(os.path.join(pathname, "btnClick.wav"))
        pygame.mixer.Sound.set_volume(soundEffect,0.5)#0.5 is the volume
        pygame.mixer.Sound.play(soundEffect,0) #play the track
            
        #load a new button image
        self.image = pygame.image.load(filepath)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(0,self.screen_height)
        #if the volume is on, it turns it off
        if not silent:
            pygame.mixer.Sound.set_volume(soundTrack,0.0)#0.0 is the volume
        else: #else it turn it on
            pygame.mixer.Sound.set_volume(soundTrack,0.5)#0.5 is the volume
        
        screen.blit(self.image, self.rect)
        

#this class manage the hay on the screen
class Hay(pygame.sprite.Sprite):
    #constructor
    def __init__(self, pos, filepath=os.path.join(pathname, 'sprites/hayl.png')):
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
    def update(self,screen, time, width):
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

def bottonClick():
    soundEffect = pygame.mixer.Sound(os.path.join(pathname, "btnClick.wav"))
    pygame.mixer.Sound.set_volume(soundEffect,0.5)#0.5 is the volume
    pygame.mixer.Sound.play(soundEffect,0) #play the track

#this is the main function
def menu(screen, silent):

    #screen is the display
    #global screen 
    width, height = 1000,600 #screens size
    #screen = pygame.display.set_mode((width,height))
    

    #initialize objects
    background = Background(width, height)
    title = Title(width//6 * 5, height//6*5)
    hay = Hay((width,450))
    
    #initialize sound track
    soundTrack = pygame.mixer.Sound(os.path.join(pathname, "startMenu.wav"))
    if not silent: pygame.mixer.Sound.set_volume(soundTrack,0.5)#0.5 is the volume
    else: pygame.mixer.Sound.set_volume(soundTrack,0.0)#0.00 is the volume
    pygame.mixer.Sound.play(soundTrack,-1)#the -1 let the sound repeates when it ends
    

    #this dictionary cointains all of the buttons 
    buttonList = {}

    btnPlay = Button(os.path.join(pathname, 'sprites/btnplay.png'), width, height//4)
    btnExit = Button(os.path.join(pathname, 'sprites/btnexit.png'), width, btnPlay.getY() + 100)
    if not silent: 
        btnMode = Button(os.path.join(pathname, 'sprites/volume.png'), width, btnExit.getY() + 100)
    else:
        btnMode = Button(os.path.join(pathname, 'sprites/mute.png'), width, btnExit.getY() + 100)
    buttonList[1] = btnPlay 
    buttonList[0] = btnExit
    buttonList[2] = btnMode
    
    #time count how many cicles the program perform
    time = 0

    endProgram = False

    
    endProgram = False
    keywords = ["inizia", "esci", "muta", "audio",
                "play"]
    start = False
    stop = False
    mute = False
    volume = False

    with sr.Microphone() as source:
        #this while loop control the screen animations
        recognizer.adjust_for_ambient_noise(source, duration=1)
        while not endProgram and (start or stop == False):
            #updates elements
            background.update(screen)
            title.update(screen)
            if hay.update(screen, time, width):
                hay = Hay((width,450))  
            btnPlay.update(screen, width, height)
            btnExit.update(screen, width, height)
            btnMode.update(screen, width, height)
            
            
            for event in pygame.event.get():
                controlExit(event)


            #update screen status
            pygame.display.update()
            time += 1

            try:
                recorded_audio = recognizer.listen(source, timeout=1)

                text = recognizer.recognize_google(
                    recorded_audio, 
                    language="it_EU"
                )
                final = text.lower().split(" ")

                if keywords[0] in final or keywords[4] in final:
                    start = True
                    endProgram = True
                    bottonClick()
                    userChoice = 1
                elif keywords[1] in final:
                    stop = True
                    endProgram = True
                    bottonClick()
                    userChoice = 0
                elif keywords[2] in final and not silent:
                    btnMode.changeStatusTo(screen, os.path.join(pathname,'sprites/mute.png'), soundTrack, silent)
                    silent = True
                elif keywords[3] in final and silent:
                    btnMode.changeStatusTo(screen, os.path.join(pathname,'sprites/volume.png'), soundTrack, silent)
                    silent = False
            except Exception:
                pass
    
    
    pygame.mixer.Sound.stop(soundTrack)
    #pygame.quit()
    return userChoice, silent

if __name__ == "__main__":
    menu()
