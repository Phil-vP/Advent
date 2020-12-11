# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:56:46 2020

@author: Philipp
"""

x = 0
x_Robot = 0
y = 0
y_Robot = 0

allX = []
allY = []
coordinates = [(0,0)]

def doSomething():
    global x
    
    with open("input.txt") as fp:
        allLines = fp.read().splitlines()
    
    line = allLines[0]
    
#    for c in line:
#        move(c)
    
    for index in range(0, len(line)-1, 2):
        move(line[index])
        moveRobot(line[index+1])
    
#    print(allX)
#    print(allY)
#    
#    print("Max X: " + str(max(allX)))
#    print("Min X: " + str(min(allX)))
#    
#    print("Max Y: " + str(max(allY)))
#    print("Min Y: " + str(min(allY)))
    
#    print(coordinates)
    
    visited = []
    count = 0
    
    for c in coordinates:
        if c not in visited:
            visited.append(c)
            count += 1
    
    print(count)
    
    
def move(c):
    global x
    global y
    
    if c == '^':
        y += 1
#        allY.append(y)
    
    elif c == 'v':
        y -= 1
#        allY.append(y)
    
    elif c == '>':
        x += 1
#        allX.append(x)
    
    elif c == '<':
        x -= 1
#        allX.append(x)
    
    else:
        print("Error with " + str(c))
    
    tupel = (x, y)
    print("Santa moves to " + str(tupel))
    coordinates.append(tupel)

def moveRobot(c):
    global x_Robot
    global y_Robot
    
    if c == '^':
        y_Robot += 1
#        allY.append(y)
    
    elif c == 'v':
        y_Robot -= 1
#        allY.append(y)
    
    elif c == '>':
        x_Robot += 1
#        allX.append(x)
    
    elif c == '<':
        x_Robot -= 1
#        allX.append(x)
    
    else:
        print("Error with " + str(c))
    
    tupel = (x_Robot, y_Robot)
    print("Robot moves to " + str(tupel))
    coordinates.append(tupel)
    
    # fout = open("output.txt", "w+")
    # fout.write("Moinsen")
    # fout.close()

if __name__== "__main__":
    doSomething()