# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 12:32:15 2020

@author: Philipp
"""
testing = False

def doSomething():
    name = "input.txt"
    global testing
    if testing:
        name = "inputTest.txt"
    with open(name) as f:
        allLines = f.readlines()
    
    for c in range(len(allLines)):
        allLines[c] = allLines[c].rstrip()
    
    for l in allLines:
        
    

if __name__== "__main__":
    doSomething()