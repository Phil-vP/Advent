# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:56:46 2020

@author: Philipp
"""

values = {}

def doSomething():

    global values
    
    with open("input.txt") as fp:
        allLines = fp.read().splitlines()
    
    lineslength = len(allLines)
    
    alreadyDone = [False] * lineslength
    
    values["->"] = -1
    values["AND"] = -1
    values["OR"] = -1
    values["LSHIFT"] = -1
    values["RSHIFT"] = -1
    values["NOT"] = -1
    
    
    while False in alreadyDone:
        for l in range(lineslength):
            if alreadyDone[l]:
                continue
            
            line = allLines[l]
            
            if not processable(line):
                continue
            
            process(line)
            alreadyDone[l] = True
        
        for l in range(lineslength):
            print("--" + str(alreadyDone[l]) + "-- line: " + allLines[l])
        
        print()
        
    k_list = list(values.keys())
    sorted_keys = k_list[6:]
    sorted_keys.sort()
    
    for k in sorted_keys:
        print(k + ": " + str(values[k]))


def process(line):
    
    global values
    
    l_split = line.split(' ')
    
    sp_length = len(l_split)
    
    if sp_length == 3:
        if l_split[0].isnumeric():
            values[l_split[2]] = int(l_split[0])
        else:
            values[l_split[2]] = values[l_split[0]]
        
        print("Zuweisung")
        return
    
    if sp_length == 4:
        
        x = values[l_split[1]]
        
        values[l_split[3]] = ~x
        
        print("NOT")
        return
    
    if sp_length == 5:
        operator = l_split[1]
        
        if not l_split[0].isnumeric():
            x = values[l_split[0]]
        else:
            x = int(l_split[0])
        target = l_split[4]
        
        if operator == "LSHIFT":
            value = int(l_split[2])
            values[target] = x << value
            return
        
        if operator == "RSHIFT":
            value = int(l_split[2])
            values[target] = x >> value
            return
        
        y = values[l_split[2]]
        
        if operator == "AND":
            
            values[target] = x & y
            return
        
        if operator == "OR":
            values[target] = x | y
            return
            
        
    
    

def processable(line):
    print("line: " + line)
    l_split = line.split(' ')
    sp_length = len(l_split)
    
#    print(l_split)
    l_split.pop(-1)
#    print(l_split)
    
    keys = list(values.keys())
    
    if sp_length == 3:
        if l_split[0].isnumeric():
            return True
    
    for sp in l_split:
        if not sp.isnumeric() and sp not in keys:
            print("Error: " + sp + " not in keys")
            return False
    
    return True
    


    # fout = open("output.txt", "w+")
    # fout.write("Moinsen")
    # fout.close()


if __name__== "__main__":
    doSomething()