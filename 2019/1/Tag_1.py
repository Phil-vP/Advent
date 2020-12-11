# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 12:32:15 2019

@author: Philipp
"""

def rechnen(zahl):
    x = int(int(zahl)/3)
    y = x-2
    return y

def alleDurchgehen():
    with open("input.txt") as fp:
        allList = fp.readlines();
    summe = 0
        
    for x in allList:
        #print(x)
        summe += rechnen(x)
    print(summe)
    
def alleDurchgehenExtraFuel():
    with open("input.txt") as fp:
        allList = fp.readlines();
    summe = 0
    #allList = [1969]
        
    for x in allList:
        y = rechnen(x)
        while y >= 0:
            #print(x)
            summe += y
            y = rechnen(y)
    print(summe)

if __name__== "__main__":
    #print(rechnen(100756))
    alleDurchgehen()