# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 12:32:15 2019

@author: Philipp
"""
def testMax():
    with open("input.txt") as fp:
        st = fp.readlines()
        #print(st)
        #print(len(st))
        first = st[0]
        second = st[1]
        firstWire = first.split(",")
        firstWire.pop()
        secondWire = second.split(",")
        secondWire.pop()
    
    currentX = 0
    maxX = 0
    minX = 0
    currentY = 0
    maxY = 0
    minY = 0
    
    for x in firstWire:
        dX = 0
        dY = 0
        if x[0] == "R":
            dX = 1
        elif x[0] == "L":
            dX = -1
        elif x[0] == "U":
            dY = 1
        elif x[0] == "D":
            dY = -1
        #print(x)
        #print(x[0])
        #print(x[1:])
        #print("-----")
        number = int(x[1:])
        currentX += number*dX
        currentY += number*dY
        
        if currentX > maxX:
            maxX = currentX
        if currentX < minX:
            minX = currentX
        
        if currentY > maxY:
            maxY = currentY
        if currentY < minY:
            minY = currentY
    
    currentX = 0
    currentY = 0
    for x in secondWire:
        dX = 0
        dY = 0
        if x[0] == "R":
            dX = 1
        elif x[0] == "L":
            dX = -1
        elif x[0] == "U":
            dY = 1
        elif x[0] == "D":
            dY = -1
        #print(x)
        #print(x[0])
        #print(x[1:])
        #print("-----")
        number = int(x[1:])
        currentX += number*dX
        currentY += number*dY
        
        if currentX > maxX:
            maxX = currentX
        if currentX < minX:
            minX = currentX
        
        if currentY > maxY:
            maxY = currentY
        if currentY < minY:
            minY = currentY
            
    print("maxX: " + str(maxX))
    print("minX: " + str(minX))
    print("maxY: " + str(maxY))
    print("minY: " + str(minY))

def doSomething():
    
    with open("input.txt") as fp:
        st = fp.readlines()
        #print(st)
        #print(len(st))
        first = st[0]
        second = st[1]
        firstWire = first.split(",")
        firstWire.pop()
        secondWire = second.split(",")
        secondWire.pop()
        
    #print(firstWire)
    #print(secondWire)
    
    grid = []
    
    xNull = 2600
    yNull = 3400
    
    for i in range(17200):
        s = [False]*11100
        grid.append(s)
    
    #First Grid
    currentX = xNull
    currentY = yNull
    
    
    for x in firstWire:
        #print("currentX: " + str(currentX))
        #print("currentY: " + str(currentY))
        #print(x[0])
        #print(x[1:])
        #print("---")
        dX = 0
        dY = 0
        if x[0] == "R":
            dX = 1
        elif x[0] == "L":
            dX = -1
        elif x[0] == "U":
            dY = 1
        elif x[0] == "D":
            dY = -1
        #print(x)
        #print(x[0])
        #print(x[1:])
        #print("-----")
        number = int(x[1:])
        for i in range(number):
            currentX += dX
            currentY += dY
            grid[currentX][currentY] = True
            if currentX < 0 or currentY < 0:
                print("ALARM")
                return
            
    print("First Wire fertig")
    
    
    currentX = xNull
    currentY = yNull
    
    distances = []
    
    
    for x in secondWire:
        dX = 0
        dY = 0
        if x[0] == "R":
            dX = 1
        elif x[0] == "L":
            dX = -1
        elif x[0] == "U":
            dY = 1
        elif x[0] == "D":
            dY = -1
        
        number = int(x[1:])
        for i in range(number):
            currentX += dX
            currentY += dY
            if grid[currentX][currentY] == True:
                distanceX = abs(currentX - xNull)
                distanceY = abs(currentY - yNull)
                total = distanceX + distanceY
                
                distances.append(total)
                
            else:
                grid[currentX][currentY] = True
            
            if currentX < 0 or currentY < 0:
                print("ALARM")
                return
            
    print("Second Wire fertig")
    print(distances)
    print(max(distances))
    print(min(distances))
 
def doSomethingSecond():
    
    with open("input.txt") as fp:
        st = fp.readlines()
        #print(st)
        #print(len(st))
        first = st[0]
        second = st[1]
        firstWire = first.split(",")
        firstWire.pop()
        secondWire = second.split(",")
        secondWire.pop()
        
    #print(firstWire)
    #print(secondWire)
    
    grid = []
    
    xNull = 2600
    yNull = 3400
    
    for i in range(17200):
        s = [0]*11100
        grid.append(s)
    
    #First Grid
    currentX = xNull
    currentY = yNull
    
    distanceFirst = 0
    for x in firstWire:
        #print("currentX: " + str(currentX))
        #print("currentY: " + str(currentY))
        #print(x[0])
        #print(x[1:])
        #print("---")
        dX = 0
        dY = 0
        if x[0] == "R":
            dX = 1
        elif x[0] == "L":
            dX = -1
        elif x[0] == "U":
            dY = 1
        elif x[0] == "D":
            dY = -1
        #print(x)
        #print(x[0])
        #print(x[1:])
        #print("-----")
        number = int(x[1:])
        for i in range(number):
            distanceFirst += 1
            currentX += dX
            currentY += dY
            grid[currentX][currentY] = distanceFirst
            if currentX < 0 or currentY < 0:
                print("ALARM")
                return
            
    print("First Wire fertig")
    
    
    currentX = xNull
    currentY = yNull
    
    distances = []
    
    distanceSecond = 0
    for x in secondWire:
        dX = 0
        dY = 0
        if x[0] == "R":
            dX = 1
        elif x[0] == "L":
            dX = -1
        elif x[0] == "U":
            dY = 1
        elif x[0] == "D":
            dY = -1
        
        number = int(x[1:])
        for i in range(number):
            distanceSecond += 1
            currentX += dX
            currentY += dY
            if grid[currentX][currentY] != 0:
                
                total = grid[currentX][currentY] + distanceSecond
                distances.append(total)
            
            if currentX < 0 or currentY < 0:
                print("ALARM")
                return
            
    print("Second Wire fertig")
    print(distances)
    print(max(distances))
    print(min(distances))
    

if __name__== "__main__":
    #test()
    doSomethingSecond()
    #testMax()