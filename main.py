from threading import Thread
import threading

import time
from Libraries.reconAudio import reconAudio
#from startMenu import generateOperations

threadLock = threading.Lock() #sync thread 

global text #result of speech-to-text func

class SpeechToText(Thread):
    def __init__(self, nome):
        Thread.__init__(self)
        self.nome = nome
        #self.durata = 5

    def run(self):
        global text

        print("start capture...")

        threadLock.acquire()
        text = reconAudio()

        if text == False:
            print("Errors has occurred in reconnaissance...")

        threadLock.release()

class GraphicInterface(Thread):
    def __init__(self, nome):
        Thread.__init__(self)
        self.nome = nome
        #self.durata = 5

    def run(self):
        print("serving graphic...")

        threadLock.acquire()

        #generateOperations(1000,600)

        threadLock.release()


threadRecon = SpeechToText("test1")
threadGraphic = GraphicInterface("test2")

threadRecon.start()
threadGraphic.start()

threadRecon.join()
threadGraphic.join()

print(text)
        





