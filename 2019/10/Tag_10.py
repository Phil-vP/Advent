# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 12:32:15 2019

@author: Philipp
"""
import math

testing = False


def laser(laserRow, laserCol):
    name = "input.txt"
    global testing
    if testing:
        name = "inputTest.txt"
    
    lines = []
    with open(name) as fp:
        lines = fp.readlines()
    #print(lines)
    
    for l in range(len(lines)):
        lines[l] = lines[l].rstrip()
        #print(l)
    rows = len(lines)
    cols = len(lines[0])
    
    table = []
    tableReihenfolge = []
    for r in range(rows):
        table.append(list(lines[r].rstrip()))
        tableReihenfolge.append(list(lines[r].rstrip()))
    print("Rows: " + str(rows))
    print("Cols: " + str(cols))
    
    currentMax = 1
    
    #obenRechts
    allVal = []
    for r in range(laserRow+1):
        for c in range(laserCol, cols):
            if r == laserRow:
                tan = 90
            else:
                tan = abs(math.degrees(math.atan((c-laserCol)/(r-laserRow))))
            if not r == laserRow or not c == laserCol:
                if table[r][c] == "#":
                    rTan = round(tan, 2)
                    allVal.append(rTan)
                    stTan = str(rTan)
                    table[r][c] = stTan
    
    valNoDouble = []
    with open("output.txt", "a+") as f:
        f.write(str(allVal))
        f.write("\n")
        for x in allVal:
            if x not in valNoDouble:
                valNoDouble.append(x)
        f.write(str(valNoDouble))
        f.write("\n")
        print(valNoDouble)
        valNoDouble.sort()
        for i in range(len(valNoDouble)):
            valNoDouble[i] = str(valNoDouble[i])
        print(valNoDouble)
        f.write(str(valNoDouble))
        f.write("\n")
    
    for r in range(laserRow+1):
        for c in range(laserCol, cols):
            if not tableReihenfolge[r][c] == "X" and not tableReihenfolge[r][c] == ".":
                tableReihenfolge[r][c] = valNoDouble.index(str(table[r][c]))+currentMax
    
    prettyOutput(table)
    prettyOutput(tableReihenfolge)
    
    currentMax += len(valNoDouble)
    
    #untenRechts
    allVal = []
    for r in range(laserRow+1, rows):
        for c in range(laserCol, cols):
            if c == laserCol:
                tan = 90
            else:
                tan = abs(math.degrees(math.atan((r-laserRow)/(c-laserCol))))
            if not r == laserRow or not c == laserCol:
                if table[r][c] == "#":
                    rTan = round(tan, 2)
                    allVal.append(rTan)
                    stTan = str(rTan)
                    table[r][c] = stTan
    
    valNoDouble = []
    with open("output.txt", "a+") as f:
        f.write(str(allVal))
        f.write("\n")
        for x in allVal:
            if x not in valNoDouble:
                valNoDouble.append(x)
        f.write(str(valNoDouble))
        f.write("\n")
        print(valNoDouble)
        valNoDouble.sort()
        for i in range(len(valNoDouble)):
            valNoDouble[i] = str(valNoDouble[i])
        print(valNoDouble)
        f.write(str(valNoDouble))
        f.write("\n")
    
    for r in range(laserRow+1, rows):
        for c in range(laserCol, cols):
            if not tableReihenfolge[r][c] == "X" and not tableReihenfolge[r][c] == ".":
                tableReihenfolge[r][c] = valNoDouble.index(str(table[r][c]))+currentMax
    
    prettyOutput(table)
    prettyOutput(tableReihenfolge)
    
    currentMax += len(valNoDouble)
    
    #untenLinks
    allVal = []
    for r in range(laserRow, rows):
        for c in range(laserCol):
            if r == laserRow:
                tan = 90
            else:
                tan = abs(math.degrees(math.atan((c-laserCol)/(r-laserRow))))
            if not r == laserRow or not c == laserCol:
                if table[r][c] == "#":
                    rTan = round(tan, 2)
                    allVal.append(rTan)
                    stTan = str(rTan)
                    table[r][c] = stTan
    
    valNoDouble = []
    with open("output.txt", "a+") as f:
        f.write(str(allVal))
        f.write("\n")
        for x in allVal:
            if x not in valNoDouble:
                valNoDouble.append(x)
        f.write(str(valNoDouble))
        f.write("\n")
        print(valNoDouble)
        valNoDouble.sort()
        for i in range(len(valNoDouble)):
            valNoDouble[i] = str(valNoDouble[i])
        print(valNoDouble)
        f.write(str(valNoDouble))
        f.write("\n")
    
    for r in range(laserRow, rows):
        for c in range(laserCol):
            if not tableReihenfolge[r][c] == "X" and not tableReihenfolge[r][c] == ".":
                tableReihenfolge[r][c] = valNoDouble.index(str(table[r][c]))+currentMax
    
    prettyOutput(table)
    prettyOutput(tableReihenfolge)
    
    currentMax += len(valNoDouble)
    
    
    #obenLinks
    allVal = []
    for r in range(laserRow):
        for c in range(laserCol):
            tan = abs(math.degrees(math.atan((r-laserRow)/(c-laserCol))))
            if not r == laserRow or not c == laserCol:
                if table[r][c] == "#":
                    rTan = round(tan, 2)
                    allVal.append(rTan)
                    stTan = str(rTan)
                    table[r][c] = stTan
    
    valNoDouble = []
    with open("output.txt", "a+") as f:
        f.write(str(allVal))
        f.write("\n")
        for x in allVal:
            if x not in valNoDouble:
                valNoDouble.append(x)
        f.write(str(valNoDouble))
        f.write("\n")
        print(valNoDouble)
        valNoDouble.sort()
        for i in range(len(valNoDouble)):
            valNoDouble[i] = str(valNoDouble[i])
        print(valNoDouble)
        f.write(str(valNoDouble))
        f.write("\n")
    
    for r in range(laserRow):
        for c in range(laserCol):
            if not tableReihenfolge[r][c] == "X" and not tableReihenfolge[r][c] == ".":
                tableReihenfolge[r][c] = valNoDouble.index(str(table[r][c]))+currentMax
    
    prettyOutput(table)
    prettyOutput(tableReihenfolge)
    
    currentMax += len(valNoDouble)
    
    
def doSomething():
    name = "input.txt"
    global testing
    if testing:
        name = "inputTest.txt"
    
    lines = []
    with open(name) as fp:
        lines = fp.readlines()
    #print(lines)
    
    for l in range(len(lines)):
        lines[l] = lines[l].rstrip()
        print(l)
    rows = len(lines)
    cols = len(lines[0])
    
    table = []
    for r in range(rows):
        table.append(list(lines[r].rstrip()))
    
    
    for t in table:
        print(t)
    
    #print("[0][1]: " + str(table[0][1]))
    #print("[1][0]: " + str(table[1][0]))
    
    prettyPrint(table)
    calc(table, rows, cols)

def calc(table, rows, cols):
    #f = open("output.txt", "w+")
    #f.write("")
    #f.close()
    print("rows: " + str(rows))
    print("cols: " + str(cols))
    tableNumbers = []
    for r in range(rows):
        x = []
        for c in range(cols):
            if table[r][c] == "#":
                x.append(0)
            else:
                x.append(".")
        tableNumbers.append(x)
    #prettyPrint(tableNumbers)
    
    maxVal = 0
    maxValRow = 0
    maxValCol = 0
    for r in range(rows):
        x = []
        for c in range(cols):
            if table[r][c] == "#":
                number = getNumberTwo(table, rows, cols, r, c)
                tableNumbers[r][c] = number
                prettyPrint(tableNumbers)
                if number > maxVal:
                    maxVal = number
                    maxValRow = r
                    maxValCol = c
                #prettyOutput(tableNumbers)
    
    print("maxVal: " + str(maxVal))
    print("maxValRow: " + str(maxValRow))
    print("maxValCol: " + str(maxValCol))
            

def getNumberTwo(table, rows, cols, myRow, myCol):
    #f = open("output.txt", "a+")
    print("===================================================")
    print("TABLE VON " + str(myRow) + "|" + str(myCol))
    print("===================================================")
    
    #f.write("===================================================\n")
    #f.write("TABLE VON " + str(myRow) + "|" + str(myCol) + "\n")
    #f.write("===================================================\n")
    #print("asdf")
    t = []
    counterAsteroids = 0
    for r in range(rows):
        x = []
        for c in range(cols):
            #if table[r][c] == "#":
                #x.append(True)
            #else:
                #x.append(False)
            x.append(table[r][c])
        t.append(x)
    
    #t[myRow][myCol] = False
    t[myRow][myCol] = "%"
    
    
    for r in range(rows):
        for c in range(cols):
            if t[r][c] == "#":
                counterAsteroids += 1
                t[r][c] = "O"
                print("-------------------------------------------")
                #f.write("-------------------------------------------\n")
                #prettyPrint(t)
                #f.close()
                #prettyOutput(t)
                print("Before cancelling")
                #f = open("output.txt", "a+")
                #f.write("Before cancelling\n")
                # Alle Asteroiden in der Sichtlinie rausnehmen
                dR1 = myRow-r
                dC1 = myCol-c
                counter = 1
                gcd = math.gcd(abs(dR1),abs(dC1))
                dR = int(dR1/gcd)
                dC = int(dC1/gcd)
                while r+(counter*dR) is not myRow or c+(counter*dC) is not myCol:
                    if t[r+counter*dR][c+counter*dC] == "#":
                        t[r+counter*dR][c+counter*dC] = "?"
                    counter += 1
                    
                #prettyPrint(t)
                #f.close()
                #prettyOutput(t)
                print("After first cancelling")
                #f = open("output.txt", "a+")
                #f.write("After first cancelling\n")
                counter = 1
                dR *= -1
                dC *= -1
                cRow = r+(counter*dR)
                cCol = c+(counter*dC)
                while cRow >= 0 and cRow < rows and cCol >= 0 and cCol < cols:
                    if t[cRow][cCol] == "#":
                        t[cRow][cCol] = "&"
                    counter += 1
                    cRow = r+(counter*dR)
                    cCol = c+(counter*dC)
                #prettyPrint(t)
                #f.close()
                #prettyOutput(t)
                print("After fully cancelling, counterAsteroid = " + str(counterAsteroids))
                #f = open("output.txt", "a+")
                #f.write("After fully cancelling, counterAsteroid = " + str(counterAsteroids) + "\n")
                t[r][c] = "-"
    return counterAsteroids
    #f.close()


def prettyPrint(table):
    print()
    #print("In prettyPrint")
    for t in table:
        s = ""
        for x in t:
            if type(x) is int:
                if x < 10:
                    s += "00"
                elif x < 100:
                    s+= "0"
            #else:
                #s += " "
            s += str(x) + "|"
        print(s)

def prettyOutput(table):
    f = open("output.txt", "a+")
    f.write("\n")
    #print("In prettyOutput")
    for t in table:
        s = ""
        for x in t:
            #if type(x) is int:
                #if x < 10:
                    #s += "0"
            #else:
                #s+= " "
            s += "{:5s}".format(str(x)) + "|"
        f.write(s + "\n")
    f.close()


if __name__== "__main__":
    f = open("output.txt", "w+")
    f.write("")
    f.close()
    #laser(3,8)
    laser(20,20)