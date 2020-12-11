# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 12:32:15 2019

@author: Philipp
"""

def getFull(eingabe):
    n = 5-len(str(eingabe))
    return n*"0" + str(eingabe)


def doSomething():
    

    with open("input.txt") as fp:
        st = fp.readline()
        
    allInt = st.split(",")
    
    #allInt = []
    #print(allInt)
    
    for x in range(len(allInt)):
        allInt[x] = int(allInt[x])
        
    opcode = 0
    pointer = 0
    
    while opcode != "99":
        fullCode = getFull(allInt[pointer])
        opcode = fullCode[3:]
        val1 = 0
        val2 = 0
        target = 0
        
        if opcode == "01": #Addieren
            
            if fullCode[2] == "0": #Position Mode
                v = allInt[pointer+1]
                val1 = allInt[v]
            else:
                val1 = allInt[pointer+1] #Immediate Mode
            
            if fullCode[1] == "0": #Position Mode
                v = allInt[pointer+2]
                val2 = allInt[v]
            else:
                val2 = allInt[pointer+2] #Immediate Mode
                
            target = allInt[pointer+3]
            allInt[target] = val1+val2
            
            pointer += 4
        
        elif opcode == "02": #Multiplizieren
            
            if fullCode[2] == "0": #Position Mode
                v = allInt[pointer+1]
                val1 = allInt[v]
            else:
                val1 = allInt[pointer+1] #Immediate Mode
            
            if fullCode[1] == "0": #Position Mode
                v = allInt[pointer+2]
                val2 = allInt[v]
            else:
                val2 = allInt[pointer+2] #Immediate Mode
                
            target = allInt[pointer+3]
            allInt[target] = val1*val2
            
            pointer += 4
            
        elif opcode == "03": #Input
            
            x = int(input("Input: "))
            v = allInt[pointer+1]
            allInt[v] = x
            
            pointer += 2
            
        elif opcode == "04": #Output
            
            if fullCode[2] == "0": #Position Mode
                v = allInt[pointer+1]
                val1 = allInt[v]
            else:
                val1 = allInt[pointer+1] #Immediate Mode
            
            print("Output: " + str(val1))
            
            pointer += 2
        
        elif opcode == "05": #Jump if true
            
            if fullCode[2] == "0": #Position Mode
                v = allInt[pointer+1]
                val1 = allInt[v]
            else:
                val1 = allInt[pointer+1] #Immediate Mode
            
            if fullCode[1] == "0": #Position Mode
                v = allInt[pointer+2]
                val2 = allInt[v]
            else:
                val2 = allInt[pointer+2] #Immediate Mode
            
            #print("In jumpIfTrue, val1= " + str(val1))
            if(val1 != 0):
                pointer = val2
            else:
                pointer += 3
                
        elif opcode == "06": #Jump if false
            
            if fullCode[2] == "0": #Position Mode
                v = allInt[pointer+1]
                val1 = allInt[v]
            else:
                val1 = allInt[pointer+1] #Immediate Mode
            
            if fullCode[1] == "0": #Position Mode
                v = allInt[pointer+2]
                val2 = allInt[v]
            else:
                val2 = allInt[pointer+2] #Immediate Mode
            
            #print("In jumpIfFalse, val1= " + str(val1))
            if(val1 == 0):
                pointer = val2
            else:
                pointer += 3
                
        elif opcode == "07": #less than
            
            if fullCode[2] == "0": #Position Mode
                v = allInt[pointer+1]
                val1 = allInt[v]
            else:
                val1 = allInt[pointer+1] #Immediate Mode
            
            if fullCode[1] == "0": #Position Mode
                v = allInt[pointer+2]
                val2 = allInt[v]
            else:
                val2 = allInt[pointer+2] #Immediate Mode
                
            x = 0
            if val1 < val2:
                x = 1
            
            target = allInt[pointer+3]
            allInt[target] = x
            
            pointer += 4
            
        elif opcode == "08": #equals
            
            if fullCode[2] == "0": #Position Mode
                v = allInt[pointer+1]
                val1 = allInt[v]
            else:
                val1 = allInt[pointer+1] #Immediate Mode
            
            if fullCode[1] == "0": #Position Mode
                v = allInt[pointer+2]
                val2 = allInt[v]
            else:
                val2 = allInt[pointer+2] #Immediate Mode
                
            x = 0
            if val1 == val2:
                x = 1
            
            target = allInt[pointer+3]
            allInt[target] = x
            
            pointer += 4
        
        elif opcode == "99": #Ende
            print("ENDE")
        
        else:
            print("Alarm, anderer opcode: " + opcode)
            break
    #print(allInt)
        

if __name__== "__main__":
    #print(getFull("01"))
    #test()
    doSomething()