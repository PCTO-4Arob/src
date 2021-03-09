import pygame, sys
import random
import os
import cv2
from pygame.locals import *
from GraphicMain.operations import *
from config import *
from time import sleep


pathname = os.path.dirname(os.path.realpath(__file__))


pygame.init()


WHITE = (255,255,255)
POSSIBLE_POSITIONS = [(WINDOW_WIDTH/4-200, WINDOW_HEIGHT/4),
                        (WINDOW_WIDTH/4-200, WINDOW_HEIGHT/4*3),
                        (WINDOW_WIDTH/4*3-200, WINDOW_HEIGHT/4),
                        (WINDOW_WIDTH/4*3-200, WINDOW_HEIGHT/4*3)]



'''------------------------------
CLASSES
-------------------------------'''
class SimpleText():
    def __init__(self, x, y, text, txtFont='freesansbold.ttf', size = 150, color = (255,255,255)):
        self.x = x
        self.y = x

        self.font = pygame.font.SysFont(txtFont, size)
        self.img = self.font.render(text, True, color)
        
    def update(self, x, y):
        #if self.rect.collidepoint(x, y):
        #    return True
        screen.blit(self.img, (self.x,self.y))
    
    def update(self, screen):
        screen.blit(self.img, (self.x,self.y))


class Button():
    #constructor
    def __init__(self, filepath, screen_width, screen_height):
        self.screen_height = screen_height
        self.screen_width = screen_width

        try:
            #load the image
            self.image = pygame.image.load(filepath)
            self.rect = self.image.get_rect()
            self.rect = self.rect.move(screen_width, self.screen_height)
        except Exception as e:
            #print the error on the screen
            print('error: ', str(e))

    #update the button status
    def collide(self,x,y):
        #controls if the user press the button
        if self.rect.collidepoint(x, y):
            return True
        else: return False        
        
    
    def update(self, screen):
        screen.blit(self.image, self.rect)


class ComplexText():
    def __init__(self, x, y, text, txtFont='freesansbold.ttf', size=150, color=WHITE, thickness=10):
        self.x = x
        self.y = y
        self.color = color
        self.thickness = thickness
        self.text = text

        self.font = pygame.font.SysFont(txtFont, size)
        self.img = self.font.render(text, True, color)
        self.rect = self.img.get_rect()
    
    def getText(self):
        return self.text
        
    def update(self,screen):
        screen.blit(self.img, (self.x,self.y))
        pygame.draw.rect(self.img, self.color, self.rect, self.thickness)
    def changeColor(self,color):
        self.color = color


class TextBox():
    def __init__(self,  x, y, text, txtFont='freesansbold.ttf', size=150, color=WHITE, thickness=10):
        self.x = x
        self.y = y
        self.txtFont = txtFont
        self.size = size
        self.thickness = thickness
        
        self.backBotton = Button(os.path.join(pathname, 'backBotton.png'), x, y)
        self.text = ComplexText( x, y, text, txtFont, size, color, thickness)

    def update(self, screen):
        # self.backBotton.update()
        self.text.update(screen)

    def isCorrect(self, result):
        if self.text.getText() == result:
            return True
        else: return False
    
    def getText(self):
        return self.text.getText()
    
    def getCordX(self):
        return self.x
    def getCordY(self):
        return self.y
    
    def changeColor(self,color):
        self.text.changeColor(color)
        


    def collide(self, x, y):
        if self.x <= WINDOW_WIDTH/2:
            if self.y <= WINDOW_HEIGHT/2: textQuarter = 4
            else: textQuarter = 3
        else:
            if self.y <= WINDOW_HEIGHT/2: textQuarter = 1
            else: textQuarter = 2
        
        if x <= WINDOW_WIDTH/2:
            if y <= WINDOW_HEIGHT/2: pointerQuarter = 4
            else: pointerQuarter = 3
        else:
            if y <= WINDOW_HEIGHT/2: pointerQuarter = 1
            else: pointerQuarter = 2

        if textQuarter == pointerQuarter:
            return True
        else:
            return False


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
    def update(self, screen):
        screen.blit(self.fullScreenImage, self.rect)


#This class contains the background method
class Counter():
    #constructor
    def __init__(self, x, y, filepath):
        try:
            #load the image
            self.image = pygame.image.load(filepath)
            self.rect = self.image.get_rect()
            self.rect = self.rect.move(x,y)
            
        except Exception as e:
            #print the exception on the screen
            print('error: ', str(e))

    #update the background status
    def update(self, screen):
        screen.blit(self.image, self.rect)


'''------------------------------
FUNCTIONS
-------------------------------'''



def initQuestion():
    x, y = random.choice(POSSIBLE_POSITIONS)
    text = createStringOperationWithSolution()
    question = TextBox(x, y, text[:-2], size=115)
    return question, text[-2:]
        

def initAnswers(result):
    answers = []
    random_value = random.randint(0,3)
    x,y = POSSIBLE_POSITIONS[random_value] 
    answers.append(TextBox(x+175, y, result, size=150))
    for i in range(4):
        if i == random_value:
            continue
        x, y = POSSIBLE_POSITIONS[i]
        text = createStringOperationWithSolution()
        answers.append(TextBox(x+175, y, text[-2:], size=150))
    
    return answers


def controlExit(event):
    if event.type == pygame.QUIT:
        quit()
        sys.exit()


def riproduceJingle(path):
    jingle = pygame.mixer.Sound(path)
    pygame.mixer.Sound.set_volume(jingle, 1)
    pygame.mixer.Sound.play(jingle)


def calculateMaxDim(conts):
    max_dim = [0, 0, 0, 0]
    for element in conts:
        x,y,w,h=cv2.boundingRect(element)
        if x + w > max_dim[1]:
            max_dim[0] = x
            max_dim[1] = x + w
            max_dim[2] = y
            max_dim[3] = y + h
    return max_dim


def calculateCounrours(img, lowerBound, upperBound, kernelClose, kernelOpen):
    #convert BGR to HSV
    imgHSV= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    # create the Mask
    mask=cv2.inRange(imgHSV,lowerBound,upperBound)
    #morphology
    maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
    maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)

    maskFinal=maskClose
    conts,h=cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    return conts


def backToMain(event):
    if event.type == pygame.QUIT:
        return True
    if event.type == pygame.KEYDOWN:
        return True
    return False