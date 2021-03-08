import random
import pygame
from pygame.locals import *
#l[0]is the result. l[1][0] and l[1][1] are the addends. l[2] is the sign (as char)
#l[result,[firstAddend,secondAddend],sign]
def createMultiplication(l):
    l[1][0] = random.randint(1,10)
    l[1][1] = random.randint(1,10) 
    l[0] = l[1][0] * l[1][1]
    l[2] = "*" 
    return l
def createDivision(l):
    l[0] = random.randint(1,10)
    l[1][1] = random.randint(1,10)
    l[1][0] = l[0] * l[1][1]
    l[2] = "/"
    return l
def createAddition(l):
    l[0] = random.randint(50,100)
    l[1][0] = random.randint(20,50)
    l[1][1] = l[0] - l[1][0]
    l[2] = "+"
    return l

def createSubtracion(l):
    
    l[0] = random.randint(0,40)
    l[1][0] = random.randint(40,100)
    l[1][1] = l[1][0] - l[0]
    l[2] = "-"
    return l
    
def createOperations():
    chose = random.randint(0,3)
    temp = [0,[0,0]," "]
    if chose == 0:
        return createMultiplication(temp)
    elif chose == 1:
        return createDivision(temp)   
    elif chose == 2:
        return createAddition(temp)
    return createSubtracion(temp)
          
    
def createStringOperationWithSolution():
    operation = createOperations()
    return (f"{operation[1][0]} {operation[2]} {operation[1][1]} = {operation[0]}")  


    
def createStringOperationWithoutSolution():
    operation = createOperations()
    return (f"{operation[1][0]} {operation[2]} {operation[1][1]} = ...")  

