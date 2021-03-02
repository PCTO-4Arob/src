import pygame
from pygame.locals import *
pygame.init()


class Background():

    def __init__(self, x, y, filepath='./sprites/background.jpg'):
        try:
            self.image = pygame.image.load(filepath)
            self.rect = self.image.get_rect()
            self.rect = self.rect.move(0,0)
            #move background
            self.fullScreenImage = pygame.transform.scale(self.image, (x*2,y))
            self.rect = self.fullScreenImage.get_rect()
        except Exception as e:
            print('error: ', str(e))

    def update(self):
        self.rect.move(self.rect.center[0]+5,self.rect.center[1])
        screen.blit(self.fullScreenImage, self.rect)


class Button():

    def __init__(self, filepath, screen_height):
        self.screen_height = screen_height
        try:
            self.image = pygame.image.load(filepath)
            self.rect = self.image.get_rect()
            self.rect = self.rect.move(0,self.screen_height)
            self.image = pygame.transform.scale(self.image, (500,100))
        except Exception as e:
            print('error: ', str(e))

    def update(self,x,y):
        if self.rect.collidepoint(x, y):
            return True
        screen.blit(self.image, self.rect)

    def changeStatus(self, imgName, x, y):
        if self.rect.collidepoint(x, y):
            try:
                self.image = pygame.image.load(imgName)
                self.rect = self.image.get_rect()
                self.rect = self.rect.move(0,self.screen_height)
                self.image = pygame.transform.scale(self.image, (500,100))
            except Exception as e:
                print('error: ', str(e))
        screen.blit(self.image, self.rect)


def controlExit(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

'''
def controlKeyPressed(event):
    if event.type==pygame.KEYDOWN:
        if event.key==K_RIGHT :
            moveRight()
            drawRob()

        if event.key==K_DOWN :
            moveDown()
            drawRob()
        if event.key==K_UP:
            moveUp()
            drawRob()
        if event.key==K_LEFT:
            moveLeft()
            drawRob()
'''
    


def menu():
    global screen 
    screen = pygame.display.set_mode((640,480), FULLSCREEN)
    width, height = screen.get_size()

    gameMode = True
    background = Background(width, height)

    buttonList = {}

    btnPlay = Button('./sprites/btnplay.png', height/3-100)
    btnExit = Button('./sprites/btnexit.png', (height/3 - 100) * 2)
    btnMode = Button('./sprites/btnmode1.png', (height/3 - 100) * 4)
    buttonList[1] = btnPlay 
    buttonList[0] = btnExit
    buttonList[2] = btnMode
    

    while True:

        background.update()
        btnPlay.update(width, height)
        btnExit.update(width, height)
        btnMode.update(width, height)
        
        for event in pygame.event.get():
            controlExit(event)
            #controlKeyPressed(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y postions of the mouse click
                for key, value in buttonList.items():
                    x, y = event.pos
                
                    print(x,y)
                    
                    if key == 2:
                        if gameMode:
                            btnMode.changeStatus('./sprites/btnmode2.png', x, y)
                        else:
                            btnMode.changeStatus('./sprites/btnmode1.png', x, y)
                        gameMode = not gameMode
                    elif value.update(x, y) == True: 
                        print(key)                   
                        return key, gameMode

        #update screen status
        pygame.display.update()
    

if __name__ == "__main__":
    menu()