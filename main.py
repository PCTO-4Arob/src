import time
import sys

from Libraries.startMenu.startMenu import menu
from GraphicMain.gameDesign import graficaPricipale

def main():

    exitMenu = -1
    exitGame = -1


    while exitMenu != 0:
       
        exitMenu = menu()
        if exitMenu == 0:
            exit(0)
        elif exitMenu == 1:
            while exitGame != 0:
                exitGame = graficaPricipale()


if __name__ == "__main__":
    main()





