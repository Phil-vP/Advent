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
        line = f.readline()
    #print(line)

    for x in range(97, 123):
        newLine = line.replace(chr(x), "")
        newLine = newLine.replace(chr(x-32), "")
        print("Replaced the letter " + chr(x))
        remove(newLine)
        print("---")

def remove(line):
    changed = True
    count = 0
    while changed:
        newLine = ""
        changed = False
        x = 0
        while x < len(line):
            if x < len(line)-1 and abs(ord(line[x])-ord(line[x+1])) == 32:
                changed = True
                x += 2
            else:
                newLine += line[x]
                x += 1
        line = newLine
        #print(newLine)
        #print(count)
        count += 1
    
    #print()
    #print(line)
    print(len(line))
    

if __name__== "__main__":
    doSomething()