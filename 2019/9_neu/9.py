# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:56:46 2020

@author: Philipp
"""

clean_code = []

code = []
index = 0
output = 0
relative_base = 0


def read_code():
    global clean_code
    
    with open("input.txt") as fp:
        allLines = fp.read().splitlines()
    
    line = allLines[0]
    
    clean_code = line.split(',')
    
    for i in range(len(clean_code)):
        clean_code[i] = int(clean_code[i])
    
    
    add_array = [0] * 5000
    clean_code.extend(add_array)


def reset_code():
    global code
    global index
    global output
    
    code = clean_code.copy()
    index = 0
    output = 0


def intcode():
    
    # Resetting status of code
    print("Running the intcode computer")
    
    while code[index] != 99:
        
        if not doOperation():
            return -1
        
        # print("Code after Operation:")
        # print(code)
        # print()
    
    return 0
    
    # fout = open("output.txt", "w+")
    # fout.write("Moinsen")
    # fout.close()

def doOperation():
#    global code
#    global index
    
    opcode_raw = code[index]
    
    st = "0" * (5 - len(str(opcode_raw)))
    
    opcode = int(opcode_raw % 100)
    
    opcode_raw = st + str(opcode_raw)
    
    print("opcode_raw: " + str(opcode_raw))
    
    if opcode == 1:
        # ADD
        op_add(opcode_raw)
        return True
    
    elif opcode == 2:
        # MULT
        op_mult(opcode_raw)
        return True
    
    elif opcode == 3:
        # INPUT
        op_input(opcode_raw)
        return True
    
    elif opcode == 4:
        # OUTPUT
        op_output(opcode_raw)
        return True
    
    elif opcode == 5:
        # JUMP IF TRUE
        op_jumpiftrue(opcode_raw)
        return True
    
    elif opcode == 6:
        # JUMP IF FALSE
        op_jumpiffalse(opcode_raw)
        return True
    
    elif opcode == 7:
        # LESS THAN
        op_lessthan(opcode_raw)
        return True
    
    elif opcode == 8:
        # EQUALS
        op_equals(opcode_raw)
        return True
    
    elif opcode == 9:
        # ADJUST RELATIVE BASE
        op_adjustRelative(opcode_raw)
        return True
    
    else:
        print("Opcode: " + str(opcode))
        print("ERROR, exiting program")
        return False



def op_add(opcode_raw):
    
    global code
    global index
    
    mode_1 = 0
    mode_2 = 0
    
    mode_index = opcode_raw[:-2]
    mode_1 = int(mode_index[2])
    mode_2 = int(mode_index[1])
    mode_ergebnis = int(mode_index[0])
        
    
    pos1 = index+1
    pos2 = index+2
    posErgebnis = index+3
    

    if mode_1 == 0:
        # Position mode
        pos1 = code[index + 1]
    
    elif mode_1 == 2:
        # Relative mode
        pos1 = relative_base + code[index + 1]
    

    if mode_2 == 0:
        # Position mode
        pos2 = code[index + 2]
    
    elif mode_2 == 2:
        # Relative mode
        pos2 = relative_base + code[index + 2]


    if mode_ergebnis == 0:
        # Position mode
        posErgebnis = code[index + 3]
    
    elif mode_ergebnis == 2:
        # Relative mode
        posErgebnis = relative_base + code[index + 3]
    
    val1 = code[pos1]
    val2 = code[pos2]
    
    ergebnis = val1 + val2
    
    code[posErgebnis] = ergebnis
    
    print("Index: " + str(index))
    # print("Using array:" + str(code[index:index+4]))
    print("Operation: Addition")
    print("Value 1: " + str(val1))
    print("Value 2: " + str(val2))
    print("Ergebnis: " + str(ergebnis) + ", written to position " + str(posErgebnis))
    print()
    
    index += 4


def op_mult(opcode_raw):
    
    global code
    global index
    
    mode_1 = 0
    mode_2 = 0
    
    mode_index = opcode_raw[:-2]
    mode_1 = int(mode_index[2])
    mode_2 = int(mode_index[1])
    mode_ergebnis = int(mode_index[0])
        
    
    pos1 = index+1
    pos2 = index+2
    posErgebnis = index+3
    

    if mode_1 == 0:
        # Position mode
        pos1 = code[index + 1]
    
    elif mode_1 == 2:
        # Relative mode
        pos1 = relative_base + code[index + 1]
    

    if mode_2 == 0:
        # Position mode
        pos2 = code[index + 2]
    
    elif mode_2 == 2:
        # Relative mode
        pos2 = relative_base + code[index + 2]


    if mode_ergebnis == 0:
        # Position mode
        posErgebnis = code[index + 3]
    
    elif mode_ergebnis == 2:
        # Relative mode
        posErgebnis = relative_base + code[index + 3]
    
    val1 = code[pos1]
    val2 = code[pos2]
    
    ergebnis = val1 * val2
    
    code[posErgebnis] = ergebnis
    
    print("Index: " + str(index))
    # print("Using array:" + str(code[index:index+4]))
    print("Operation: Multiplication")
    print("Value 1: " + str(val1))
    print("Value 2: " + str(val2))
    print("Ergebnis: " + str(ergebnis) + ", written to position " + str(posErgebnis))
    print()
    
    index += 4


def op_input(opcode_raw):
    
    global code
    global index
    
    ##
    mode = int(str(opcode_raw)[2])
    
    pos = index+1
    
    if mode == 0:
        # Position mode
        pos = code[index+1]
    
    elif mode == 2:
        # Relative mode
        pos = relative_base + code[index + 1]
    
    value = input("Input please: ")
    
    if not value.isnumeric():
        print("Error: Value is not numeric")
        return
    
    value_int = int(value)
    code[pos] = value_int
    
    print("Index: " + str(index))
    print("Operation: Input")
    print("Value: " + str(value_int))
    print("Saved input to position " + str(pos))
    print()
    
    index += 2


def op_output(opcode_raw):
    
    global index
    global output
    
    ##
    mode = int(str(opcode_raw)[2])
    
    pos = index+1
    
    if mode == 0:
        # Position mode
        pos = code[index+1]
    
    elif mode == 2:
        # Relative mode
        pos = relative_base + code[index + 1]
    
    value = code[pos]
    output = value
    
    fout = open("output.txt", "a+")
    # fout.write("OUTPUT by instruction of index " + str(index) + ": ")
    fout.write(str(value) + "\n")
    fout.close()
    
    print("Index: " + str(index))
    print("Operation: Output")
    print("Value at position " + str(pos) + ": ")
    print("########")
    print(str(value))
    print("########")
    print()
    
    index += 2


def op_jumpiftrue(opcode_raw):
    
    global index
    
    mode_1 = 0
    mode_2 = 0
    
    mode_index = opcode_raw[:-2]
    mode_1 = int(mode_index[2])
    mode_2 = int(mode_index[1])
        
    
    pos1 = index+1
    pos2 = index+2
    

    if mode_1 == 0:
        # Position mode
        pos1 = code[index+1]
    
    elif mode_1 == 2:
        # Relative mode
        pos1 = relative_base + code[index + 1]
    

    if mode_2 == 0:
        # Position mode
        pos2 = code[index+2]
    
    elif mode_2 == 2:
        # Relative mode
        pos2 = relative_base + code[index + 2]
    
    
    val1 = code[pos1]
    val2 = code[pos2]
    
    print("Index: " + str(index))
    # print("Using array:" + str(code[index:index+4]))
    print("Operation: Jump-If-True")
    print("Value: " + str(val1))
    print("Target: " + str(val2))
    
    if val1 != 0:
        index = val2
        print("Jump successful")
    else:
        index += 3
        print("Jump skipped")
    
    print()


def op_jumpiffalse(opcode_raw):
    
    global index
    
    mode_1 = 0
    mode_2 = 0
    
    mode_index = opcode_raw[:-2]
    mode_1 = int(mode_index[2])
    mode_2 = int(mode_index[1])
        
    
    pos1 = index+1
    pos2 = index+2
    

    if mode_1 == 0:
        # Position mode
        pos1 = code[index+1]
    
    elif mode_1 == 2:
        # Relative mode
        pos1 = relative_base + code[index + 1]
    

    if mode_2 == 0:
        # Position mode
        pos2 = code[index+2]
    
    elif mode_2 == 2:
        # Relative mode
        pos2 = relative_base + code[index + 2]
    
    
    val1 = code[pos1]
    val2 = code[pos2]
    
    print("Index: " + str(index))
    # print("Using array:" + str(code[index:index+4]))
    print("Operation: Jump-If-False")
    print("Value: " + str(val1))
    print("Target: " + str(val2))
    
    if val1 == 0:
        index = val2
        print("Jump successful")
    else:
        index += 3
        print("Jump skipped")
    
    print()


def op_lessthan(opcode_raw):
    
    global code
    global index
    
    mode_1 = 0
    mode_2 = 0
    
    mode_index = opcode_raw[:-2]
    mode_1 = int(mode_index[2])
    mode_2 = int(mode_index[1])
    mode_ergebnis = int(mode_index[0])
        
    
    pos1 = index+1
    pos2 = index+2
    posErgebnis = index+3
    

    if mode_1 == 0:
        # Position mode
        pos1 = code[index + 1]
    
    elif mode_1 == 2:
        # Relative mode
        pos1 = relative_base + code[index + 1]
    

    if mode_2 == 0:
        # Position mode
        pos2 = code[index + 2]
    
    elif mode_2 == 2:
        # Relative mode
        pos2 = relative_base + code[index + 2]


    if mode_ergebnis == 0:
        # Position mode
        posErgebnis = code[index + 3]
    
    elif mode_ergebnis == 2:
        # Relative mode
        posErgebnis = relative_base + code[index + 3]
    
    val1 = code[pos1]
    val2 = code[pos2]
    
    ergebnis = 0
    if val1 < val2:
        ergebnis = 1
    
    code[posErgebnis] = ergebnis
    
    print("Index: " + str(index))
    # print("Using array:" + str(code[index:index+4]))
    print("Operation: Less Than")
    print("Value 1: " + str(val1))
    print("Value 2: " + str(val2))
    print("Ergebnis: " + str(ergebnis) + ", written to position " + str(posErgebnis))
    print()
    
    index += 4


def op_equals(opcode_raw):
    
    global code
    global index
    
    mode_1 = 0
    mode_2 = 0
    
    mode_index = opcode_raw[:-2]
    mode_1 = int(mode_index[2])
    mode_2 = int(mode_index[1])
    mode_ergebnis = int(mode_index[0])
        
    
    pos1 = index+1
    pos2 = index+2
    posErgebnis = index+3
    

    if mode_1 == 0:
        # Position mode
        pos1 = code[index + 1]
    
    elif mode_1 == 2:
        # Relative mode
        pos1 = relative_base + code[index + 1]
    

    if mode_2 == 0:
        # Position mode
        pos2 = code[index + 2]
    
    elif mode_2 == 2:
        # Relative mode
        pos2 = relative_base + code[index + 2]


    if mode_ergebnis == 0:
        # Position mode
        posErgebnis = code[index + 3]
    
    elif mode_ergebnis == 2:
        # Relative mode
        posErgebnis = relative_base + code[index + 3]
    
    val1 = code[pos1]
    val2 = code[pos2]
    
    ergebnis = 0
    
    if val1 == val2:
        ergebnis = 1
    
    code[posErgebnis] = ergebnis
    
    print("Index: " + str(index))
    # print("Using array:" + str(code[index:index+4]))
    print("Operation: Equals")
    print("Value 1: " + str(val1))
    print("Value 2: " + str(val2))
    print("Ergebnis: " + str(ergebnis) + ", written to position " + str(posErgebnis))
    print()
    
    index += 4


def op_adjustRelative(opcode_raw):
    
    global index
    global relative_base
    
    mode = int(str(opcode_raw)[2])
    
    pos = index+1
    

    if mode == 0:
        # Position mode
        pos = code[index+1]
    
    elif mode == 2:
        # Relative mode
        pos = relative_base + code[index + 1]
    
    value = code[pos]
    
    print("Index: " + str(index))
    print("Operation: Adjust relative base")
    print("Old relative base: " + str(relative_base))
    print("Value: " + str(value))
    
    relative_base += value
    
    print("New relative base: " + str(relative_base))
    print()
    
    index += 2
    

def do_before(a, b):
    global code
    
    code[1] = a
    code[2] = b


def do_stuff():
    fout = open("output.txt", "w+")
    fout.write("")
    fout.close()
    
    read_code()
    reset_code()
    print("Program exited with code " + str(intcode()))


if __name__== "__main__":
    
    do_stuff()