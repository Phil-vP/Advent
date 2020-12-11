# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 12:32:15 2019

@author: Philipp
"""
testing = False

def rechnen(zahl):
    x = int(int(zahl)/3)
    y = x-2
    return y

def doSomething():
    name = "input.txt"
    global testing
    if testing:
        name = "inputTest.txt"
    with open(name) as f:
        allLines = f.readlines()
    summe = 0
    allVal = []
    found = False
    counter = 0
    while not found:
        print("Durchlauf " + str(counter))
        counter += 1
        for l in allLines:
            l = l.rstrip()
            summe += int(l)
            if summe in allVal:
                found = True
                print(str(summe) + " gefunden!")
                break
            allVal.append(summe)
    
        
    

if __name__== "__main__":
    doSomething()