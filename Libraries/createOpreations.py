import random
#l[0]is the result. l[1][0] and l[1][1] are the addends. l[2] is the sign (as char)
#l[result,[firstAddend,saecondAddend],sign]
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
    
def createOpearions():
    operations = []
    for n in range(4):
        chose = random.randint(0,4)
        temp = [0,[0,0]," "]
        if chose == 0:
            operations.append(createMultiplication(temp))
        elif chose == 1:
            operations.append(createDivision(temp))   
        elif chose == 3:
            operations.append(createAddition(temp))
        else:  
            operations.append(createSubtracion(temp))
    return operations
          
    

print( createOpearions())