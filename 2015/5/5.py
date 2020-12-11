# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:56:46 2020

@author: Philipp
"""


def doSomething():
    
    with open("input.txt") as fp:
        allLines = fp.read().splitlines()
    
    count = 0
    
    for l in allLines:
        if isNiceB(l):
            count += 1
    
    
    print(count)


def isNiceB(line):
    containList = []
    
    contain = False
    repeat = False
    
    for i in range(len(line) - 1):
        a = line[i]
        b = line[i+1]
        
        combined = a + "" + b
        
        if not contain:
            if combined in containList:
                if i > 0:
                    z = line[i-1]
                    if not z+a == a+b:
                        contain = True
            
            containList.append(combined)
            
        
        if not repeat and i < len(line)-2:
            c = line[i+2]
            repeat = (c == a)
    
    return repeat & contain
        
            
        

def isNice(line):
    
    checkList = ["ab", "cd", "pq", "xy"]
    vowels = ["a", "e", "i", "o", "u"]
    
    numberVowels = 0
    double = False
    
    for i in range(len(line) - 1):
        a = line[i]
        b = line[i+1]
        
        combined = a + "" + b
        
        if combined in checkList:
            return False
        
        if a == b:
            double = True
        
        if a in vowels:
            numberVowels += 1
    
    if b in vowels:
        numberVowels += 1
    
    if numberVowels >= 3 and double:
        return True
    
    return False
        
        

if __name__== "__main__":
    doSomething()