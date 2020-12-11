# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:56:46 2020

@author: Philipp
"""

global allLines

def doSomething():
    global allLines
    
    with open("input.txt") as fp:
        allLines = fp.read().splitlines()
    
    
    total = 1
    
    total *= slope(1, 1)
    total *= slope(3, 1)
    total *= slope(5, 1)
    total *= slope(7, 1)
    total *= slope(1, 2)
    
    print("Total: " + str(total))
    
    print("Count: " + str(slope(1, 1)))
    print("Count: " + str(slope(3, 1)))
    print("Count: " + str(slope(5, 1)))
    print("Count: " + str(slope(7, 1)))
    print("Count: " + str(slope(1, 2)))
    


def slope(x, y):
    current_x = x
    current_y = y
    
    depth = len(allLines)
    length = len(allLines[0])
    
    count = 0
        
    while current_y < depth:
        # print(allLines[current_y][current_x])
        if allLines[current_y][current_x] == "#":
            count += 1
        
        current_y += y
        current_x += x
        current_x %= length
    
    # fout = open("output.txt", "w+")
    # fout.write("Moinsen")
    # fout.close()
    # print("Count: " + str(count))
    return count

if __name__== "__main__":
    doSomething()