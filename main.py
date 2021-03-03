from threading import Thread
import threading
import time

from Libraries.traceTest import objectTracking

threadLock = threading.Lock() #sync thread 

class ObjectRecon(Thread):
    def __init__(self, nome):
        Thread.__init__(self)
        self.nome = nome
        self.durata = 5
        self.tempCord = []

    def run(self):
        print("start capture...")
        
        threadLock.acquire()
        self.tempCord = objectTracking()
        time.sleep(self.durata)
        threadLock.release()

    def getCord(self):
        return self.tempCord



class GraphicMenu(Thread):
    def __init__(self, nome):
        Thread.__init__(self)
        self.nome = nome
        self.initiateGame = False
        #self.durata = 5

    def run(self):
        print("serving graphic menu...")

        threadLock.acquire()

        #self.initiateGame = #funzionetomatis

        threadLock.release()

    def getStart(self):
        return self.initiateGame

class GraphicGame(Thread):
    def __init__(self,nome):
        Thread.__init__(self)
        self.nome = nome
        self.startGraphic
    
    def run(self):
        print("serving graphic interface...")

        #self.startGraphic = funzione fenoglio


def main():
    
    menu = GraphicMenu("startMenu")

    if menu.initiateGame == True:
        #chiama parte fenoglio
        #chiama parte recon
        #ripeti



    
    #print(player.getCord())

    







if __name__ == "__main__":
    main()





