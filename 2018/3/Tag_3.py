# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 12:32:15 2020

@author: Philipp
"""
testing = False
size = 1000

def doSomething():
    name = "input.txt"
    global testing
    if testing:
        name = "inputTest.txt"
    with open(name) as f:
        allLines = f.readlines()
    
    for c in range(len(allLines)):
        allLines[c] = allLines[c].rstrip()
    
    global size
    field = []
    for x in range(size):
        y = [0]*size
        field.append(y)
    
    for l in allLines:
        line = l.split(" ")
        offset = line[2].split(",")
        colOffset = int(offset[0])
        rowOffset = offset[1]
        rowOffset = int(rowOffset[:-1])
        
        span = line[3].split("x")
        colSpan = int(span[0])
        rowSpan = int(span[1])
        colEnd = colOffset + colSpan
        rowEnd = rowOffset + rowSpan
        
        #print("------------------")
        #print("Line:")
        #print(l)
        #print("colOffset: " + str(colOffset))
        #print("rowOffset: " + str(rowOffset))
        #print("colSpan: " + str(colSpan))
        #print("rowSpan: " + str(rowSpan))
        
        for r in range(rowOffset, rowEnd):
            for c in range(colOffset, colEnd):
                field[r][c] += 1
    
    counter = 0
    for x in field:
        for y in x:
            if y > 1:
                counter += 1
    print("Counter: " + str(counter))
    for l in allLines:
        line = l.split(" ")
        offset = line[2].split(",")
        colOffset = int(offset[0])
        rowOffset = offset[1]
        rowOffset = int(rowOffset[:-1])
        
        span = line[3].split("x")
        colSpan = int(span[0])
        rowSpan = int(span[1])
        colEnd = colOffset + colSpan
        rowEnd = rowOffset + rowSpan
        
        onlyOne = True
        
        for r in range(rowOffset, rowEnd):
            for c in range(colOffset, colEnd):
                if field[r][c] != 1:
                    onlyOne = False
        if onlyOne:
            print(l)

if __name__== "__main__":
    doSomething()