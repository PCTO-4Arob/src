from threading import Thread
import threading

import time
from Libraries.reconAudio import reconAudio
#from startMenu import generateOperations

threadLock = threading.Lock() #sync thread 

global text #result of speech-to-text func
global list
global startSpeechToText

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

        startSpeechToText = #funzione tomatis
        #generateOperations(1000,600)

        threadLock.release()


def main():
    global list, text

    graphic = GraphicInterface("MainGraphicInterface")
    graphic.start()

    list = []

    speech1 = SpeechToText("sp1")
    speech2 = SpeechToText("sp2")
    speech3 = SpeechToText("sp3")
    speech4 = SpeechToText("sp4")
    speech5 = SpeechToText("sp5")

    if startSpeechToText == 1:
        speech1.start()
        speech1.join()
        list[0] = text

        speech2.start()
        speech2.join()
        list[1] = text

        speech3.start()
        speech3.join()
        list[2] = text

        speech4.start()
        speech4.join()
        list[3] = text

        speech5.start()
        speech5.join
        list[4] = text







if __name__ == "__main__":
    main()





