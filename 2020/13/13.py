# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:56:46 2020

@author: Philipp
"""

def doSomething():
    
    with open("input.txt") as fp:
        allLines = fp.read().splitlines()
    
    
    allNumbers = allLines[1].split(',')
    totalLength = len(allNumbers) - 1
    allNumbersNoX = []
    
    for i in allNumbers:
        if i != 'x':
            allNumbersNoX.append(int(i))
    
    ally = {}
    allM = {}
    alla = {}
    
    m = 1
    for i in allNumbersNoX:
        m *= i
    
    for m_i in allNumbersNoX:
        M = int(m / m_i)
        allM[m_i] = M
        
        ally[m_i] = getY(M, m_i)
        
        alla[m_i] = totalLength - allNumbers.index(str(m_i))
    
    
    print("y * M = 1 mod m")
    
    for m_i in allNumbersNoX:
        print(str(ally[m_i]) + " * " + str(allM[m_i]) + " = 1 mod " + str(m_i) + ", a = " + str(alla[m_i]))
    
    
    ergebnis = 0
    for m_i in allNumbersNoX:
        ergebnis += alla[m_i] * ally[m_i] * allM[m_i]
    
    ergebnis_mod = ergebnis % m
    print("Ergebnis: " + str(ergebnis))
    print("Ergebnis mod: " + str(ergebnis_mod))
    print("Ergebnis mod kleinster Wert: " + str(ergebnis_mod - totalLength))
    
    
    

def getY(M, m):
    
    y = 1
    rest = (M * y) % m
    
    while rest != 1:
        y += 1
        rest = (M * y) % m
    
    return y
        






def ex_a():
    arrival = int(allLines[0])
    
    print("Arrival: " + str(arrival))
    
    allNumbers = []
    
    l_sp = allLines[1].split(',')
    
    for s in l_sp:
        if s != 'x':
            allNumbers.append(int(s))
    
    print(allNumbers)
    
    numberMap = {}
    
    for num in allNumbers:
        number = num
        while number < arrival:
            number += num
        
        numberMap[num] = number - arrival
    
    for num in allNumbers:
        print("Num: " + str(num) + ", diff: " + str(numberMap[num]))
        
    
    # fout = open("output.txt", "w+")
    # fout.write("Moinsen")
    # fout.close()

if __name__== "__main__":
    doSomething()
#    print(getY(221, 19))