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
    #print(allLines)
    for c in range(len(allLines)):
        allLines[c] = allLines[c].rstrip()
    #print(allLines)
    #doOne(allLines)
    doTwo(allLines)



def doTwo(allLines):
    r = len(allLines)
    length = len(allLines[0])
    for x in range(r):
        one = allLines[x]
        for y in range(x, r):
            two = allLines[y]
            similar = ""
            counterDifferent = 0
            for c in range(length):
                if one[c] == two[c]:
                    similar += one[c]
                else:
                    counterDifferent += 1
            if counterDifferent == 1:
                print(one)
                print(two)
                print(similar)
                print("-------------------")
    

def doOne(allLines):    
    counter2 = 0
    counter3 = 0
    
    for l in allLines:
        two = False
        three = False
        for x in l:
            c = l.count(x)
            if c == 2:
                two = True
            elif c == 3:
                three = True
        if two:
            counter2 += 1
        if three:
            counter3 += 1
    print("Counter2: " + str(counter2))
    print("Counter3: " + str(counter3))
    print("Mult: " + str(counter2*counter3))
    

if __name__== "__main__":
    doSomething()