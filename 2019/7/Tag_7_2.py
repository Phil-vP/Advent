# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 12:32:15 2019

@author: Philipp
"""
import itertools

running = True
testing = True


class amplifier:
    
    def __init__(self):
        self.allInt = []
        name = "input.txt"
        global testing
        if testing:
            name = "inputTest.txt"
    
        with open(name) as fp:
            st = fp.readline()
            
        self.allInt = st.split(",")
        
        for x in range(len(self.allInt)):
            self.allInt[x] = int(self.allInt[x])

    def getFull(self, eingabe):
        n = 5-len(str(eingabe))
        return n*"0" + str(eingabe)
    
    def doSomething(self, in1, in2):
        
        benutzt = False
        out = 0
        
        #allInt = []
        #print(self.allInt)
            
        opcode = 0
        pointer = 0
        
        while opcode != "99":
            fullCode = self.getFull(self.allInt[pointer])
            opcode = fullCode[3:]
            val1 = 0
            val2 = 0
            target = 0
            
            if opcode == "01": #Addieren
                
                if fullCode[2] == "0": #Position Mode
                    v = self.allInt[pointer+1]
                    val1 = self.allInt[v]
                else:
                    val1 = self.allInt[pointer+1] #Immediate Mode
                
                if fullCode[1] == "0": #Position Mode
                    v = self.allInt[pointer+2]
                    val2 = self.allInt[v]
                else:
                    val2 = self.allInt[pointer+2] #Immediate Mode
                    
                target = self.allInt[pointer+3]
                self.allInt[target] = val1+val2
                
                pointer += 4
            
            elif opcode == "02": #Multiplizieren
                
                if fullCode[2] == "0": #Position Mode
                    v = self.allInt[pointer+1]
                    val1 = self.allInt[v]
                else:
                    val1 = self.allInt[pointer+1] #Immediate Mode
                
                if fullCode[1] == "0": #Position Mode
                    v = self.allInt[pointer+2]
                    val2 = self.allInt[v]
                else:
                    val2 = self.allInt[pointer+2] #Immediate Mode
                    
                target = self.allInt[pointer+3]
                self.allInt[target] = val1*val2
                
                pointer += 4
                
            elif opcode == "03": #Input
                
                #x = int(input("Input: "))
                if not benutzt:
                    x = int(in1)
                    benutzt = True
                else:
                    x = int(in2)
                v = self.allInt[pointer+1]
                self.allInt[v] = x
                
                pointer += 2
                
            elif opcode == "04": #Output
                
                if fullCode[2] == "0": #Position Mode
                    v = self.allInt[pointer+1]
                    val1 = self.allInt[v]
                else:
                    val1 = self.allInt[pointer+1] #Immediate Mode
                
                print("Output: " + str(val1))
                return out
                
                pointer += 2
            
            elif opcode == "05": #Jump if true
                
                if fullCode[2] == "0": #Position Mode
                    v = self.allInt[pointer+1]
                    val1 = self.allInt[v]
                else:
                    val1 = self.allInt[pointer+1] #Immediate Mode
                
                if fullCode[1] == "0": #Position Mode
                    v = self.allInt[pointer+2]
                    val2 = self.allInt[v]
                else:
                    val2 = self.allInt[pointer+2] #Immediate Mode
                
                #print("In jumpIfTrue, val1= " + str(val1))
                if(val1 != 0):
                    pointer = val2
                else:
                    pointer += 3
                    
            elif opcode == "06": #Jump if false
                
                if fullCode[2] == "0": #Position Mode
                    v = self.allInt[pointer+1]
                    val1 = self.allInt[v]
                else:
                    val1 = self.allInt[pointer+1] #Immediate Mode
                
                if fullCode[1] == "0": #Position Mode
                    v = self.allInt[pointer+2]
                    val2 = self.allInt[v]
                else:
                    val2 = self.allInt[pointer+2] #Immediate Mode
                
                #print("In jumpIfFalse, val1= " + str(val1))
                if(val1 == 0):
                    pointer = val2
                else:
                    pointer += 3
                    
            elif opcode == "07": #less than
                
                if fullCode[2] == "0": #Position Mode
                    v = self.allInt[pointer+1]
                    val1 = self.allInt[v]
                else:
                    val1 = self.allInt[pointer+1] #Immediate Mode
                
                if fullCode[1] == "0": #Position Mode
                    v = self.allInt[pointer+2]
                    val2 = self.allInt[v]
                else:
                    val2 = self.allInt[pointer+2] #Immediate Mode
                    
                x = 0
                if val1 < val2:
                    x = 1
                
                target = self.allInt[pointer+3]
                self.allInt[target] = x
                
                pointer += 4
                
            elif opcode == "08": #equals
                
                if fullCode[2] == "0": #Position Mode
                    v = self.allInt[pointer+1]
                    val1 = self.allInt[v]
                else:
                    val1 = self.allInt[pointer+1] #Immediate Mode
                
                if fullCode[1] == "0": #Position Mode
                    v = self.allInt[pointer+2]
                    val2 = self.allInt[v]
                else:
                    val2 = self.allInt[pointer+2] #Immediate Mode
                    
                x = 0
                if val1 == val2:
                    x = 1
                
                target = self.allInt[pointer+3]
                self.allInt[target] = x
                
                pointer += 4
            
            elif opcode == "99": #Ende
                print("ENDE")
                global running
                running = False
                return out
            
            else:
                print("Alarm, anderer opcode: " + opcode)
                break
        #print(self.allInt)

def perm():
    werte = []
    #x = list(itertools.permutations('56789'))
    #for l in x:
        #werte.append(makeCombination(l[0], l[1], l[2], l[3], l[4]))
        #print(l)
    werte.append(makeCombination(9,8,7,6,5))
    print(werte)
    print(max(werte))
    
def makeCombination(in1, in2, in3, in4, in5):
    amp1 = amplifier()
    amp2 = amplifier()
    amp3 = amplifier()
    amp4 = amplifier()
    amp5 = amplifier()
    
    global running
    running = True
    out = amp1.doSomething(in1, 0)
    while True:
        out = amp2.doSomething(in2, out)
        if not running:
            return out
        out = amp3.doSomething(in3, out)
        if not running:
            return out
        out = amp4.doSomething(in4, out)
        if not running:
            return out
        out = amp5.doSomething(in5, out)
        if not running:
            return out
        out = amp1.doSomething(in1, out)
        if not running:
            return out
    return -1

if __name__== "__main__":
    #print(getFull("01"))
    #test()
    #doSomething()
    perm()