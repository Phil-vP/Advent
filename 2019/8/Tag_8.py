# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 12:32:15 2019

@author: Philipp
"""

testing = False
col = 25
row = 6

def layers():
    print("layers")
    
    name = "input.txt"
    global testing
    if testing:
        name = "inputTest.txt"
    
    line = ""
    with open(name) as fp:
        line = fp.readline()
    allInts = list(line)
    
    print(allInts)
    print(len(allInts))
    
    numberOfLayers = int(len(allInts)/(col*row))
    print("Number of layers: " + str(numberOfLayers))
    
    layers = []
    
    counter = 0
    
    for i in range(numberOfLayers):
        l = []
        for j in range(row):
            c = []
            for k in range(col):
                c.append(allInts[counter])
                counter += 1
            l.append(c)
        layers.append(l)
    
    for l in layers:
        for r in l:
            print(r)
        print()
    
    #minLayer(layers)
    decode(layers)

def decode(layers):
    print("In decode")
    masterLayer = []
    global row
    global col
    
    for r in range(row):
        column = []
        for c in range(col):
            for l in layers:
                st = str(l[r][c])
                if st != "2":
                    column.append(st)
                    break
                
        masterLayer.append(column)
        #print(column)
    for r in masterLayer:
        line = ""
        for e in r:
            if e == "1":
                line += chr(0x2588)
            else:
                line += " "
        print(line)
    
    print("Ende decode")
    
    
    
def minLayer(layers):
    index = 0
    minIndex = 0
    min0 = 100
    for l in layers:
        count0 = 0
        for r in l:
            for e in r:
                if str(e) == "0":
                    count0 += 1
        if count0 < min0:
            min0 = count0
            minIndex = index
        index += 1
    print("minIndex: " + str(minIndex))
    print("min0: " + str(min0))
    
    lay = layers[minIndex]
    print("The magic layer:")
    
    for r in lay:
        print(r)
    print()
    
    count1 = 0
    count2 = 0
    for r in lay:
        for e in r:
            if str(e) == "1":
                count1 += 1
            elif str(e) == "2":
                count2 += 1
    
    mul = count1*count2
    print("Ergebnis: " + str(mul))
    

if __name__== "__main__":
    layers()