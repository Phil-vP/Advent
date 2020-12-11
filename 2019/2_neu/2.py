# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:56:46 2020

@author: Philipp
"""

clean_code = []

code = []
index = 0


def read_code():
    global clean_code
    
    with open("input.txt") as fp:
        allLines = fp.read().splitlines()
    
    line = allLines[0]
    
    clean_code = line.split(',')
    
    for i in range(len(clean_code)):
        clean_code[i] = int(clean_code[i])


def reset_code():
    global code
    global index
    
    code = clean_code.copy()
    index = 0


def intcode():
    
    # Resetting status of code
    print("Running the intcode computer")
    
    while code[index] != 99:
        
        if not doOperation():
            return -1
        
        print("Code after Operation:")
        print(code)
        print()
    
    return 0
    
    # fout = open("output.txt", "w+")
    # fout.write("Moinsen")
    # fout.close()

def doOperation():
#    global code
#    global index
    
    opcode = code[index]
    
    if opcode == 1:
        # ADD
        op_add()
        return True
    
    elif opcode == 2:
        # MULT
        op_mult()
        return True
    
    else:
        print("Opcode: " + str(opcode))
        print("ERROR, exiting program")
        return False



def op_add():
    
    global code
    global index

    pos1 = code[index+1]
    pos2 = code[index+2]
    posErgebnis = code[index+3]
    
    val1 = code[pos1]
    val2 = code[pos2]
    
    ergebnis = val1 + val2
    
    code[posErgebnis] = ergebnis
    
    print("Index: " + str(index))
    print("Using array:" + str(code[index:index+4]))
    print("Operation: Addition")
    print("Value 1: " + str(val1))
    print("Value 2: " + str(val2))
    print("Ergebnis: " + str(ergebnis) + ", written to position " + str(posErgebnis))
    print()
    
    index += 4


def op_mult():
    
    global code
    global index

    pos1 = code[index+1]
    pos2 = code[index+2]
    posErgebnis = code[index+3]
    
    val1 = code[pos1]
    val2 = code[pos2]
    
    ergebnis = val1 * val2
    
    code[posErgebnis] = ergebnis
    
    print("Index: " + str(index))
    print("Using array:" + str(code[index:index+4]))
    print("Operation: Multiplication")
    print("Value 1: " + str(val1))
    print("Value 2: " + str(val2))
    print("Ergebnis: " + str(ergebnis) + "written to position " + str(posErgebnis))
    print()
    
    index += 4


def do_before(a, b):
    global code
    
    code[1] = a
    code[2] = b


def do_stuff():
    read_code()
    
    for i in range(40):
        for j in range(50):
            reset_code()
            do_before(i,j)
            print("i: " + str(i))
            print("j: " + str(j))
            intcode()
            print("After:")
            print(code[:10])
            if code[0] == 19690720:
                print("Success with " + str(i) + ", " + str(j))
                return
#            print("Program exited with code " + str(intcode()))
    print("No success yet")

if __name__== "__main__":
    
    do_stuff()