from threading import Thread
import threading
import time
import sys

from Libraries.traceTest import objectTracking
from Libraries.startMenu.startMenu import menu

def main():

    exitGame = 1

    while exitGame != 0:
       
        exitGame = menu()
        if exitGame == 0:
            exit(0)

        



    

if __name__ == "__main__":
    main()





