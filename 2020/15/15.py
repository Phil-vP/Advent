# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:56:46 2020

@author: Philipp
"""

def doSomething():
    
    with open("input.txt") as fp:
        allLines = fp.read().splitlines()
    
    allNumbers = []
    indizes = {}
    
    # targetNumber = 2020
    targetNumber = 30000000
    
    alreadyVisited = [False] * targetNumber
    
    for l in allLines[0].split(','):
        allNumbers.append(int(l))
    
    for i in range(len(allNumbers)-1):
        indizes[allNumbers[i]] = i+1
        alreadyVisited[allNumbers[i]] = True
        
    
    
    currentLastNumber = allNumbers[-1]
    
    for i in range(len(allNumbers)+1, targetNumber+1):
        
        numberAppend = 0
        
        if alreadyVisited[currentLastNumber]:
            index_last = indizes[currentLastNumber]
            numberAppend = (i-1) - index_last
        else:
            alreadyVisited[currentLastNumber] = True
        
        indizes[currentLastNumber] = i-1
        
        if i % 10000 == 0:
            print(str(i) + " durch")
        
        currentLastNumber = numberAppend
    
    print("Turn " + str(targetNumber) + ": " + str(currentLastNumber) + " appended to list\n")
    

if __name__== "__main__":
    doSomething()