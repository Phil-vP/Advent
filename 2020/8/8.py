# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:56:46 2020

@author: Philipp
"""

from datetime import datetime

accumulator = 0
currentLine = 0
executed = []


def doSomethingB():
    
    global executed
    global accumulator
    global currentLine
    
    with open("input.txt") as fp:
        allLinesOriginal = fp.read().splitlines()
    
    # fout = open("output.txt", "w+")
    # fout.write("Moinsen")
    # fout.close()
    
    for i in range(len(allLinesOriginal)):
        
#        with open("input.txt") as fp:
#            allLines = fp.read().splitlines()
        
        allLines = allLinesOriginal.copy()
            
        i_split = allLines[i].split(' ')
        
        if i_split[0] == "nop":
            allLines[i] = "jmp " + i_split[1]
        elif i_split[0] == "jmp":
            allLines[i] = "nop " + i_split[1]
        else:
            continue
    
        success = False
        accumulator = 0
        currentLine = 0
        
        linesLength = len(allLines)
        executed = [False] * linesLength
        
        while not executed[currentLine]:
            executed[currentLine] = True
            processLine(allLines[currentLine])
            
            if currentLine == linesLength:
                print("Success!")
                success = True
                break
        
        if success:
            print("Success found when switching line " + str(i))
            break
    
    print("Final Accumulator: " + str(accumulator))

def doSomethingA():
    
    global executed
    
    with open("input.txt") as fp:
        allLines = fp.read().splitlines()
    
    # fout = open("output.txt", "w+")
    # fout.write("Moinsen")
    # fout.close()
    
    linesLength = len(allLines)
    executed = [False] * linesLength
    
    while not executed[currentLine]:
        executed[currentLine] = True
        processLine(allLines[currentLine])
    
    print("Final Accumulator: " + str(accumulator))


def processLine(line):
    global accumulator
    global currentLine
    
    line_split = line.split(' ')
    call = line_split[0]
    value = int(line_split[1])
    
    if call == "nop":
        currentLine += 1
    
    elif call == "acc":
        accumulator += value
        currentLine += 1
    
    elif call == "jmp":
        currentLine += value
    
    else:
        print("ERROR")

if __name__== "__main__":
    start = datetime.now()
    
    doSomethingB()
    
    print("Time: ")
    print(datetime.now() - start)