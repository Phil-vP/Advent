# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:56:46 2020

@author: Philipp
"""

waypointRelativeX = 10
waypointRelativeY = 1


def doSomething():
    global waypointRelativeX
    global waypointRelativeY
    
    with open("input.txt") as fp:
        allLines = fp.read().splitlines()
    
    
    currentX = 0
    currentY = 0
    
    for l in allLines:
        letter = l[0]
        value = int(l[1:])
        
        if letter == 'N':
            waypointRelativeY += value
        
        elif letter == 'S':
            waypointRelativeY -= value
        
        elif letter == 'W':
            waypointRelativeX -= value
        
        elif letter == 'E':
            waypointRelativeX += value
        
        elif letter == 'L':
            amount = int(value/90)
            for i in range(amount):
                wX = waypointRelativeX
                wY = waypointRelativeY
    
                waypointRelativeX = wY * (-1)
                waypointRelativeY = wX
        
        elif letter == 'R':
            amount = int(value/90)
            for i in range(amount):
                wX = waypointRelativeX
                wY = waypointRelativeY
    
                waypointRelativeX = wY
                waypointRelativeY = wX * (-1)
        
        elif letter == 'F':
            currentX += value * waypointRelativeX
            currentY += value * waypointRelativeY
        
        else:
            print("Error")
        
        print("current Position: " + str(currentX) + "|" + str(currentY))
        print("current Waypoint: " + str(waypointRelativeX) + "|" + str(waypointRelativeY))
        print()
    
    
    print("Final X: " + str(currentX))
    print("Final Y: " + str(currentY))
    print("Manhattan: " + str(abs(currentX) + abs(currentY)))

    
    

def ex_a():
    directions = ['N', 'E', 'S', 'W']
    direction_facing = 1
    
    for l in allLines:
        letter = l[0]
        value = int(l[1:])
        direction_moving = letter
        
        print(l)
        print(letter + " - " + str(value))
        
        if letter == 'R':
            amount = int(value/90)
            direction_facing += amount
            direction_facing %= 4
            continue
        
        if letter == 'L':
            amount = int(value/90)
            direction_facing += 4
            direction_facing -= amount
            direction_facing %= 4
            continue
        
        if letter == 'F':
            direction_moving = directions[direction_facing]
        
        if direction_moving == 'N':
            currentY += value
        
        elif direction_moving == 'S':
            currentY -= value
        
        elif direction_moving == 'W':
            currentX -= value
        
        elif direction_moving == 'E':
            currentX += value
        
        else:
            print("Error in direction_moving")
    
    
    print("Final X: " + str(currentX))
    print("Final Y: " + str(currentY))
    print("Manhattan: " + str(abs(currentX) + abs(currentY)))
        
    
    
    # fout = open("output.txt", "w+")
    # fout.write("Moinsen")
    # fout.close()

if __name__== "__main__":
    doSomething()