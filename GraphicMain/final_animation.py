from GraphicMain.operations import *
from GraphicMain.classAndFunctions import *
from time import sleep
import os

pathname = os.path.dirname(os.path.realpath(__file__))


def final_animation( screen, surf_title, posBlue, posRed, winRed, all_sprites):
    
    numberSpriters=pygame.sprite.Group()
    
    
    surf_title.update(screen)
    all_sprites.draw(screen)
    numberSpriters.draw(screen)
    sleep(10)
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
    sleep(10)
    fire = pygame.mixer.Sound(os.path.join(pathname, "theme/fire.wav"))#upload the gun sound
    pygame.mixer.Sound.set_volume(fire,1)
    pygame.mixer.Sound.play(fire)
    if winRed == False:
        #CHANGES blue with a tombstone
        tombstone = pygame.sprite.Sprite(all_sprites)
        tombstone.image = pygame.image.load(os.path.join(pathname ,"Sprites/tombstone.png")).convert_alpha()
        tombstone.rect = spr_blueReverse.image.get_rect()
        tombstone.rect.x = spr_blueReverse.rect.x 
        tombstone.rect.y = spr_blueReverse.rect.y 
        spr_blueReverse.kill()
    else:
        #CHANGES red with a tombstone
        tombstone = pygame.sprite.Sprite(all_sprites)
        tombstone.image = pygame.image.load(os.path.join(pathname ,"Sprites/tombstone.png")).convert_alpha()
        tombstone.rect = spr_redReverse.image.get_rect()
        tombstone.rect.x = spr_redReverse.rect.x 
        tombstone.rect.y = spr_redReverse.rect.y 
        spr_redReverse.kill()
    
    surf_title.update(screen)
    all_sprites.draw(screen)
    numberSpriters.draw(screen)
    sleep(10)

    return