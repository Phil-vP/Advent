# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:56:46 2020

@author: Philipp
"""

def doSomething():
    
    with open("input.txt") as fp:
        allLines = fp.read().splitlines()
    
    
    id_list = []
    seat_list = [False] * 900
    
    for l in allLines:
        rows = l[:6]
        columns = l[7:]
#        print(l + ": " + rows + " " + columns)
        
        lower_row = 0
        upper_row = 128
        
#        print("   " + str(lower_row) + " - " + str(upper_row))
        
        for r in rows:
            length_half = int( (upper_row - lower_row) / 2 )
            
            if r == "F":
                upper_row -= length_half
            else:
                lower_row += length_half
            
#            print(r + ": " + str(lower_row) + " - " + str(upper_row))
        
        row = upper_row - 1
        
        if l[6] == "F":
            row = lower_row
        
#        print("Row: " + str(row))
#        print()
        
        
        
        
        lower_col = 0
        upper_col = 8
        
#        print("   " + str(lower_col) + " - " + str(upper_col))
        
        for c in columns:
            length_half = int( (upper_col - lower_col) / 2 )
            
            if c == "L":
                upper_col -= length_half
            else:
                lower_col += length_half
            
#            print(r + ": " + str(lower_col) + " - " + str(upper_col))
        
        column = upper_col - 1
        
        if l[6] == "F":
            column = lower_col
        
#        print("Column: " + str(column))
        
        
        seat_id = row * 8 + column                
#        print("Seat ID: " + str(seat_id))
#        print()
        
        id_list.append(seat_id)
        seat_list[seat_id] = True
    
    
#    print("Max: " + str(max(id_list)))
    
    for i in range(900):
        if not seat_list[i]:
            print(i)
    
    # fout = open("output.txt", "w+")
    # fout.write("Moinsen")
    # fout.close()

if __name__== "__main__":
    doSomething()