import pygame
import numpy as np
import datetime
import sys
import cv2
import importlib
from pygame.locals import *
from time import sleep
from GraphicMain.operations import *
from GraphicMain.classAndFunctions import *

import os

pathname = os.path.dirname(os.path.realpath(__file__))




DIMCOW=(310, 510)# dimension of cowboy image
DIMTOMB=(300, 300)


def controlCord(answer, prec_answer):
    if prec_answer.getCordY() - answer.getCordY() <= 200 and prec_answer.getCordX() - answer.getCordX() <= 200:
       return True
    else: return False



def finalShoot(all_sprites, spr_ToChange):
    tombstone = pygame.sprite.Sprite(all_sprites)
    tombstone.image = pygame.image.load(os.path.join(pathname ,"Sprites/tombstone.png")).convert_alpha()
    tombstone.rect = spr_ToChange.image.get_rect()
    tombstone.rect.x = spr_ToChange.rect.x 
    tombstone.rect.y = spr_ToChange.rect.y + (DIMCOW[1]-DIMTOMB[1])
    spr_ToChange.kill()
    return all_sprites


def print_group(group,screen):
    for sprite in group:
        screen.blit(sprite.image, (sprite.rect.x,sprite.rect.y))
    pygame.display.update()
        


def final_animation( screen, surf_title, winRed, all_sprites,spr_red, spr_blue,numberSpriters):
    
    cv2.destroyAllWindows()
    
    
    '''
    surf_title.update(screen)
    all_sprites.draw(screen)
    numberSpriters.draw(screen)
    '''


    spr_redReverse = pygame.sprite.Sprite(all_sprites)
    spr_redReverse.image = pygame.image.load(os.path.join(pathname, "Sprites/redCowBoyInverted.png")).convert_alpha()
    spr_redReverse.rect = spr_red.image.get_rect()
    spr_redReverse.rect.x = spr_red.rect.x 
    spr_redReverse.rect.y = spr_red.rect.y 
    spr_red.kill()


    #blue
    spr_blueReverse = pygame.sprite.Sprite(all_sprites)
    spr_blueReverse.image = pygame.image.load(os.path.join(pathname, "Sprites/blueCowBoy.png")).convert_alpha()
    spr_blueReverse.rect = spr_blue.image.get_rect()
    spr_blueReverse.rect.x = spr_blue.rect.x 
    spr_blueReverse.rect.y = spr_blue.rect.y 
    spr_blue.kill()

    surf_title.update(screen)
    all_sprites.draw(screen)
    numberSpriters.draw(screen)

    print_group(all_sprites,screen)

    #screen.blit(spr_redReverse.image, (spr_redReverse.rect.x,spr_redReverse.rect.y))
    #pygame.display.update()

    

    sleep(1)

    #GENERATE GO SIGNAL
    number = pygame.sprite.Sprite(numberSpriters)
    number.image = pygame.image.load(os.path.join(pathname, "Sprites/counter"+str(5)+".png")).convert_alpha()
    number.image = pygame.transform.scale(number.image , (100,100))
    number.rect = number.image.get_rect()
    number.rect.x =WINDOW_WIDTH /2-(100/2)
    number.rect.y =10




    #count became 0 to permit to exit the while loop
    surf_title.update(screen)
    all_sprites.draw(screen)
    numberSpriters.draw(screen)
    sleep(1)
    fire = pygame.mixer.Sound(os.path.join(pathname, "theme/fire.wav"))#upload the gun sound
    pygame.mixer.Sound.set_volume(fire,1)
    pygame.mixer.Sound.play(fire)
    

    if winRed:
        all_sprites = finalShoot(all_sprites, spr_blueReverse)
    else:
        #CHANGES red with a tombstone
        all_sprites = finalShoot(all_sprites, spr_redReverse)

    sleep(1)
    surf_title.update(screen)
    all_sprites.draw(screen)
    numberSpriters.draw(screen)
    print_group(all_sprites,screen)
    sleep(1)

    return



def mainGraphic(screen):
    
    lowerBound=np.array([33,80,40])
    upperBound=np.array([102,255,255])

    cam= cv2.VideoCapture(0)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, WINDOW_WIDTH)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, WINDOW_HEIGHT)
    kernelOpen=np.ones((5,5))
    kernelClose=np.ones((20,20))


    listCord = [0, 0]

    
    x=1000 #dimensioni basi
    y=600

    #SCREEN TO COMMENT ALL---------------------------------------------------------------------------------------------------------------
    
    pygame.init()
    #global screen
    #screen= pygame.display.set_mode((x, y))#create screen
    
    #song
    soundTrack = pygame.mixer.Sound(os.path.join(pathname, "theme/fight.wav"))
    pygame.mixer.Sound.set_volume(a,0.4)#0.6 is volume
    pygame.mixer.Sound.play(a,-1)#with -1 sound will restart forever

    #CREATION SPRITES-------------------------------------------------------------------------------------------------------
    all_sprites = pygame.sprite.Group()
    numberSpriters=pygame.sprite.Group()

    #red cowboy
    spr_red = pygame.sprite.Sprite(all_sprites)
    spr_red.image = pygame.image.load(os.path.join(pathname, "Sprites/redCowBoyYou.png")).convert_alpha()

    spr_red.rect = spr_red.image.get_rect()

    #position
    spr_red.rect.x = WINDOW_WIDTH/2-DIMCOW[0] 
    spr_red.rect.y = WINDOW_HEIGHT-DIMCOW[1]

    

    #blue cowboy
    spr_blue = pygame.sprite.Sprite(all_sprites)
    spr_blue.image = pygame.image.load(os.path.join(pathname, "Sprites/blueCowBoyInverted.png")).convert_alpha()
    spr_blue.rect = spr_red.image.get_rect()

    #position
    spr_blue.rect.x = WINDOW_WIDTH / 2 
    spr_blue.rect.y = WINDOW_HEIGHT-DIMCOW[1]
    
    
    #background 
    surf_title = Background(WINDOW_WIDTH, WINDOW_HEIGHT, os.path.join(pathname, 'Background/sfondo.jpg'))  
   
    #screen.blit(surf_tile, (0, 0))#show the background
    count=1# count  will be use to stroke for cowboy
    
    gameStatus = 0

    move = False
    selected_question = False
    answered = False
    timer = False
    winRed = 1

    while count > 0 and count <= 5:
        #drawing sprites     
        #draw these two group of sprites
        surf_title.update(screen)
        all_sprites.draw(screen)
        numberSpriters.draw(screen)
        
        if gameStatus == 0 and count < 5:
            question, result = initQuestion()
            question.update(screen)
            gameStatus = 1
        elif gameStatus == 1:
            question.update(screen)
            answers = initAnswers(result)
            gameStatus = 2
        elif gameStatus == 2:
            question.update(screen)
            if selected_question:
                gameStatus = 3
                selected_question = False
        elif gameStatus == 3:
            for answer in answers:
                answer.update(screen)
            if answered:
                gameStatus = 0
                count += 1
                move = True
                answered = False
                selected_question = False
        
        ret, img=cam.read()
        img=cv2.resize(img,(WINDOW_WIDTH,WINDOW_HEIGHT))

        #convert BGR to HSV
        imgHSV= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        # create the Mask
        mask=cv2.inRange(imgHSV,lowerBound,upperBound)
        #morphology
        maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
        maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)

        maskFinal=maskClose
        conts,h=cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

        cv2.drawContours(img,conts,-1,(255,0,0),3)

        max_dim = [0, 0, 0, 0]
        for element in conts:
            x,y,w,h=cv2.boundingRect(element)
            if x + w > max_dim[1]:
                max_dim[0] = x
                max_dim[1] = x + w
                max_dim[2] = y
                max_dim[3] = y + h

        if max_dim[1] >= 400:

            center_x = max_dim[0] + ((max_dim[1] - max_dim[0]) / 2)
            center_y = max_dim[2] + ((max_dim[3] - max_dim[2]) / 2) 


            listCord[0] = center_x
            listCord[1] = center_y

            
                
            if listCord != [0,0]:
                if question.collide(x,y) and not selected_question:
                    if not timer:
                        timer = True
                        start_time = datetime.datetime.now()
                    elif datetime.datetime.now() >= start_time + datetime.timedelta(seconds=5):
                        selected_question = True
                        timer = False
                        firstAnswer = True
                if not answered and selected_question:
                    if not timer:
                        start_time = datetime.datetime.now()
                        timer = True
                    else:
                        for answer in answers:
                            if firstAnswer:
                                prec_answer = answer
                                firstAnswer = False
                            if answer.collide(x,y) and not answered and controlCord(answer, prec_answer):
                            
                                prec_answer = answer
                                answer.changeColor((255,255,0))
                                pygame.display.update()
                            else:
                                answer.changeColor((255,255,255))
                            
                            if datetime.datetime.now() >= start_time + datetime.timedelta(seconds=5):
                                if answer.isCorrect(result):
                                    answered = True
                                    jingle = pygame.mixer.Sound(os.path.join(pathname, 'theme/correctAnswer.wav'))
                                    pygame.mixer.Sound.set_volume(jingle, 1)
                                    pygame.mixer.Sound.play(jingle)
                                else:
                                    jingle = pygame.mixer.Sound(os.path.join(pathname, 'theme/wrongAnswer.wav'))
                                    pygame.mixer.Sound.set_volume(jingle, 1)
                                    pygame.mixer.Sound.play(jingle)
                                    winRed = 0
                                    count = 5
                                timer = False
                                firstAnswer = True
                
            rect = pygame.Rect(max_dim[0], max_dim[2], max_dim[1], max_dim[3])
            pygame.draw.rect(screen,WHITE, rect,1) 
            cv2.waitKey(10)
            
        else:
            pass

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:#if you quit program will not cush
                pygame.quit()
                sys.exit()

        
            
        if count<5 and count>0:
            #COWBOYS POSISTION CHANGES--------------------------------------------------------------------------------------- 
            if move:
                spr_blue.rect.x += int(WINDOW_WIDTH/20)#RIGHT

                spr_red.rect.x -= int(WINDOW_WIDTH/20)#LEFT
                move = False
            
            #number counter-------------------------------------------------------------------------------------------
            
            number = pygame.sprite.Sprite(numberSpriters)
            number.image = pygame.image.load(os.path.join(pathname, "Sprites/counter"+str(count)+".png")).convert_alpha()
            number.image = pygame.transform.scale(number.image , (100,100))
            number.rect = number.image.get_rect()
            number.rect.x = WINDOW_WIDTH /2-(100/2)
            number.rect.y =10
            
           
    
        elif count==5:
            #TURN COWBOY-----------------------------------------------------------------
            final_animation(screen,surf_title,winRed,all_sprites,spr_red,spr_blue,numberSpriters)
            cv2.destroyAllWindows()
            pygame.mixer.music.stop()#stop music
            count=0
        
    #end while
    pygame.mixer.Sound.stop(soundTrack)
    return 0
#end main

if __name__ == "__main__":
	main()