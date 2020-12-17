# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:56:46 2020

@author: Philipp
"""

field_size = 25
start_x = 9
start_y = 9
start_z = 9
start_w = 9

field = []
char_on = "#"
char_off_on = "+"
char_off = "."
char_on_off = "-"
turns = 6

def doSomething():
    global field
    
    fout = open("output.txt", "w+")
    fout.write("")
    
    with open("input.txt") as fp:
        allLines = fp.read().splitlines()
    
    
    for w in range(field_size):
        w_f = []
        for f in range(field_size):
            dimension = []
            for p in range(field_size):
                row = [char_off] * field_size
                dimension.append(row)
            w_f.append(dimension)
        field.append(w_f)
    
    
    for y in range(len(allLines)):
        l = allLines[y]
        # print(l)
        l = l.replace('.', char_off)
        l = l.replace('#', char_on)
        # print(l)
        
        for x in range(len(l)):
            # field[start_z][y+start_y][x+start_x] = int(l[x])
            field[start_w][start_z][y+start_y][x+start_x] = l[x]
            # print("Set " + str(start_z) + "|" + str(y+start_y) + "|" + str(x+start_x) + " to " + str(l[x]))
    
    fout.write("Initial field:\n")
    outputField(fout)
    
    for r in range(turns):
        for w in range(field_size):
            for z in range(field_size):
                for y in range(field_size):
                    for x in range(field_size):
                        current_char = field[w][z][y][x]
                        count_nei = countNeighbors(x, y, z, w)
                        
                        if current_char == char_on:
                            # print("I have " + str(count_nei) + " neighbors")
                            if not (count_nei == 2 or count_nei == 3):
                                field[w][z][y][x] = char_on_off
                                # print("Switching")
                            # else:
                                # print("Remaining active")
                        
                        else:
                            if count_nei == 3:
                                field[w][z][y][x] = char_off_on
        # printField()
        # outputField(fout)
        
        for w in range(field_size):
            for z in range(field_size):
                for y in range(field_size):
                    for x in range(field_size):
                        point = field[w][z][y][x]
                        if point == char_on_off:
                            field[w][z][y][x] = char_off
                        elif point == char_off_on:
                            field[w][z][y][x] = char_on
        
        print("Done with turn " + str(r))
        
        # printField()
        # fout.write("\n################################\n")
        # fout.write("After " + str(r+1) + " cycles: \n")
        # outputField(fout)
    
                        
                    
    
    # printField()
    fout.write("\n################################\n")
    fout.write("Final after " + str(turns) + " cycles: \n")
    outputField(fout)
        
    
    
    
    
    
    
    
    print("Count: " + str(countInField()))
    
    fout.close()
    
    # print(field)
    
    

def countInField():
    summe = 0
    for w in field:
        for z in w:
            for f in z:
                summe += f.count(char_on)
                summe += f.count(char_on_off)
        
    return summe

def countOnLayer(z_in):
    summe = 0
    z = field[0][z_in]
    for f in z:
        summe += f.count(char_on)
        summe += f.count(char_on_off)
        
    # return summe
    return 1
    

def printField():
    for z in range(field_size):
        print("\nField for z = " + str(z) + ":")
        for y_1 in range(field_size):
            st = "".join(field[0][z][y_1])
            print(str(y_1) + ": " + st)


def outputField(fout):
    for z in range(field_size):
        if countOnLayer(z) == 0:
            continue
        fout.write("\nField for z = " + str(z) + ":\n")
        for y_1 in range(field_size):
            st = "".join(field[0][z][y_1])
            fout.write(str(y_1) + ": " + st + "\n")
    
    fout.write("\n################\n")

def countNeighbors(x_in, y_in, z_in, w_in):
    summe = 0
    min_x = x_in-1
    max_x = x_in+2
    if x_in == 0:
        min_x = 0
    if x_in == field_size-1:
        max_x = x_in+1
    
    min_y = y_in-1
    max_y = y_in+2
    if y_in == 0:
        min_y = 0
    if y_in == field_size-1:
        max_y = y_in+1
    
    min_z = z_in-1
    max_z = z_in+2
    if z_in == 0:
        min_z = 0
    if z_in == field_size-1:
        max_z = z_in+1
    
    min_w = w_in-1
    max_w = w_in+2
    if w_in == 0:
        min_w = 0
    if w_in == field_size-1:
        max_w = w_in+1
    
    # print("x_in: " + str(x_in) + ", min_x: " + str(min_x) +  ", max_x: " + str(max_x))
    # print("y_in: " + str(y_in) + ", min_y: " + str(min_y) +  ", max_y: " + str(max_y))
    # print("z_in: " + str(z_in) + ", min_z: " + str(min_z) +  ", max_z: " + str(max_z))
    
    for w in range(min_w, max_w):
        for z in range(min_z, max_z):
            for y in range(min_y, max_y):
                # print("z: " + str(z) + ", y: " + str(y))
                summe += field[w][z][y][min_x : max_x].count(char_on)
                summe += field[w][z][y][min_x : max_x].count(char_on_off)
    
    if field[w_in][z_in][y_in][x_in] == char_on:
        summe -= 1
    
    return summe

if __name__== "__main__":
    doSomething()