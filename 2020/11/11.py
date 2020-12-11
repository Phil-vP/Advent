# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:56:46 2020

@author: Philipp
"""

def doSomething():
    
    with open("input.txt") as fp:
        allLines = fp.read().splitlines()
    
    allSeats = []
    for line in allLines:
        allSeats.append(list(line))
    
    numberRows = len(allSeats)
    numberCols = len(allSeats[0])
        
    print("Initial state:")
    for row in allSeats:
        print(''.join(row))
    print()
    
    newSeats = []
    for row in allSeats:
        newSeats.append(row.copy())
    # newSeats = allSeats.copy()
    
    changed = True
    
    runde = 1
    
    rowRange = range(numberRows)
    colRange = range(numberCols)
    
    # for runde in range(5):
    while changed:
        
        changed = False
        
        for row in range(numberRows):
            for col in range(numberCols):
                
                currentSeat = allSeats[row][col]
                
                numberOccupied = 0
                
                for dRow in range(-1, 2):
                    for dCol in range(-1, 2):
                        if dRow == 0 and dCol == 0:
                            continue
                        mult = 0
                        ended = False
                        
                        while not ended:
                            mult += 1
                            newRow = row  + dRow * mult
                            newCol = col  + dCol * mult
                            
                            if newRow not in rowRange or newCol not in colRange:
                                ended = True
                                break
                            
                            if allSeats[newRow][newCol] == '#':
                                numberOccupied += 1
                                ended = True
                                break
                            
                            if allSeats[newRow][newCol] == 'L':
                                ended = True
                                break
                            
                            
                
                # print("Row: Start: " + str(row_start) + ", End: " + str(row_end))
                # print("Col: Start: " + str(col_start) + ", End: " + str(col_end))
                
                
                if currentSeat == 'L':
                    if numberOccupied == 0:
                        newSeats[row][col] = '#'
                        changed = True
                
                if currentSeat == '#':
                    if numberOccupied >= 5:
                        newSeats[row][col] = 'L'
                        changed = True
        
        allSeats = []
        for r in newSeats:
            allSeats.append(r.copy())
        
        print("After round " + str(runde) + ":")
        for row in allSeats:
            print(''.join(row))
        print()
        runde += 1
    
    numberOccupied = 0
    for row in allSeats:
        numberOccupied += row.count('#')
    
    print()
    print("Number of occupied seats: " + str(numberOccupied))





def ex_a():
    # for round in range(5):
    while changed:
        
        changed = False
        
        for row in range(numberRows):
            for col in range(numberCols):
                            
                row_start = row-1
                if row == 0:
                    row_start = row
                
                row_end = row+2
                if row == numberRows-1:
                    row_end = row+1
                
                col_start = col-1
                if col == 0:
                    col_start = col
                
                col_end = col+2
                if col == numberCols-1:
                    col_end = col+1
                
                # print("Row: Start: " + str(row_start) + ", End: " + str(row_end))
                # print("Col: Start: " + str(col_start) + ", End: " + str(col_end))
                
                currentSeat = allSeats[row][col]
                
                countArray = []
                
                # print("Row: " + str(row) + ", Col: " + str(col))
                for i in range(row_start, row_end):
                    # for j in range(col_start, col_range+1):
                    countArray.extend(allSeats[i][col_start:col_end])
                    # print(allSeats[i][col_start:col_end])
                
                # print(countArray)
                # print()
                
                if currentSeat == 'L':
                    if countArray.count('#') == 0:
                        newSeats[row][col] = '#'
                        changed = True
                
                if currentSeat == '#':
                    if countArray.count('#') >= 5:
                        newSeats[row][col] = 'L'
                        changed = True
        
        allSeats = []
        for r in newSeats:
            allSeats.append(r.copy())
        
        print("After round " + str(runde) + ":")
        for row in allSeats:
            print(''.join(row))
        print()
        runde += 1
    
    numberOccupied = 0
    for row in allSeats:
        numberOccupied += row.count('#')
    
    print()
    print("Number of occupied seats: " + str(numberOccupied))
                
                
    # fout = open("output.txt", "w+")
    # fout.write("Moinsen")
    # fout.close()

if __name__== "__main__":
    doSomething()