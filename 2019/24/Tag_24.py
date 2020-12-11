# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 10:56:01 2020

@author: Philipp
"""

import math


testing = False


def doSomething():
    name = "input.txt"
    global testing
    if testing:
        name  = "inputTest.txt"
    with open(name) as f:
        lines = f.readlines()
    
    field = []
    
    for l in lines:
        field.append(list(l.strip()))
    
    allStrings = []
    allStrings.append(stringify(field))
    found = False
    
    for y in field:
        print("".join(y))
    print("----------------------")
    x = 0
    
    while not found:
    #for x in range(5):
        newFeld = []
        for r in range(5):
            newList = []
            for c in range(5):
                sub = ""
                if r > 0:
                    sub += str(field[r-1][c])
                if r < 4:
                    sub += str(field[r+1][c])
                if c > 0:
                    sub += str(field[r][c-1])
                if c < 4:
                    sub += str(field[r][c+1])
                num = sub.count("#")
                
                if field[r][c] == "#":
                    if num != 1:
                        newList.append(".")
                        #newList.append(str(num))
                    else:
                        newList.append("#")
                        #newList.append(str(num))
                else:
                    if num == 1 or num == 2:
                        newList.append("#")
                        #newList.append(str(num))
                    else:
                        newList.append(".")
                        #newList.append(str(num))
            newFeld.append(newList)
        field = newFeld
        print("After " + str(x+1) + " minutes:")
        x+= 1
        
        for y in newFeld:
            print("".join(y))
        print("----------------------")
        string = stringify(newFeld)
        if string in allStrings:
            print("gefunden!")
            found = True
        allStrings.append(string)
    
    
    for s in allStrings:
        print(s)
    
    print("Gefunden:")
    for y in field:
        print("".join(y))
    
    print("Biodiversity:")
    print(getDiv(field))


def getDiv(field):
    div = 0
    for r in range(5):
        for c in range(5):
            if field[r][c] == "#":
                div += math.pow(2, (r*5)+c)
    return div

def stringify(liste):
    string = ""
    for x in liste:
        string += "".join(x)
    return string

if __name__== "__main__":
    doSomething()