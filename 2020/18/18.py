# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:56:46 2020

@author: Philipp
"""

line_split = []

def doSomething():
    global line_split
    
    with open("input.txt") as fp:
        allLines = fp.read().splitlines()
    
    sumList = []
    
    for l in allLines:
        # ergebnis = calculate(l.split(' '), 0)[0]
        prepared = prepareLine(l)
        line_split = prepared.split(' ')
        ergebnis = calculate_A(line_split)
        print(ergebnis)
        sumList.append(ergebnis)
    
    print("Summe: " + str(sum(sumList)))
        
    
    # fout = open("output.txt", "w+")
    # fout.write("Moinsen")
    # fout.close()




def calculate_A(line):
    print(line)
    currentIndex = 0
    val1 = line[0]
    
    if val1 == "(":
        counter = 1
        index = 0
        while counter != 0:
            index += 1
            char = line[currentIndex + index]
            print("Char: " + char)
            if char == "(":
                counter += 1
            elif char == ")":
                counter -= 1
            print("Counter: " + str(counter))
            print("New index: " + str(index))
            print()
        
        print("Substring: " + str(line[(currentIndex+1):(currentIndex+index)]))
        print("Klammer von Index " + str(currentIndex) + " bis " + str(currentIndex+index))
        
        val1_int = calculate_A(line[(currentIndex+1):(currentIndex+index)])
        currentIndex += index+1
    
    else:
        val1_int = int(val1)
        currentIndex += 1
    
    # Now we have the initial value
    
    while currentIndex < len(line)-1:
        print("val1_int: " + str(val1_int))
        
        operator = line[currentIndex]
        
        val2 = line[currentIndex + 1]
        
        print("Operator: " + operator)
        print("val2: " + val2)
        
        if val2 == "(":
            currentIndex += 1
            
            counter_2 = 1
            index = 0
            while counter_2 != 0:
                index += 1
                char = line[currentIndex + index]
                print("Char: " + char)
                if char == "(":
                    counter_2 += 1
                elif char == ")":
                    counter_2 -= 1
                print("Counter_2: " + str(counter_2))
                print("New index: " + str(index))
                print()
            
            print("Substring: " + str(line[(currentIndex+1):(currentIndex+index)]))
            print("Klammer von Index " + str(currentIndex) + " bis " + str(currentIndex+index))
            
            val2_int = calculate_A(line[(currentIndex+1):(currentIndex+index)])
            currentIndex += index
        
        else:
            val2_int = int(val2)
            currentIndex += 1
        
        
        if operator == '+':
            print("Calculating: " + str(val1_int) + " + " + str(val2_int) + " = " + str(str(val1_int + val2_int)))
            val1_int += val2_int
        else:
            print("Calculating: " + str(val1_int) + " * " + str(val2_int) + " = " + str(str(val1_int * val2_int)))
            val1_int *= val2_int
        
        currentIndex += 1
    
    print("Returning value of Klammer: " + str(val1_int) + "\n")
    return val1_int




def prepareLine(line):
    print(line)
    final = []
    
    for sp in line.split(' '):
        if sp == "+" or sp == "*" or sp.isnumeric():
            final.append(sp)
            continue
        
        counter = 0
        if sp[0] == "(":
            while not sp[counter].isnumeric():
                # final.extend(["0", "+", "("])
                final.append("(")
                counter += 1
            final.append(sp[counter:])
            continue
        
        if sp[-1] == ")":
            while sp[counter].isnumeric():
                counter += 1
            final.append(sp[:counter])
            for i in range(counter, len(sp)):
                final.append(")")
    
    return " ".join(final)
            

if __name__== "__main__":
    doSomething()
    # print(prepareLine("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"))
    # calculate1(prepareLine("2 + (3 + 5 * 4) - 3 + (7 + 3)").split(" "))