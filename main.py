import time
import sys
import pygame
from Libraries.startMenu.startMenu import menu
from GraphicMain.gameDesign import mainGraphic
pygame.init()

def main():

    exitMenu = -1
    exitGame = -1
    silent = False
    global screen
    screen = pygame.display.set_mode((1000,600))

    while exitMenu != 0:
       
        exitMenu, silent = menu(screen, silent)
        if exitMenu == 0:
            exit(0)
        elif exitMenu == 1:
            mainGraphic(screen, silent)


if __name__ == "__main__":
    main()





