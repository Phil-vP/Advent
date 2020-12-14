# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:56:46 2020

@author: Philipp
"""

from numpy import binary_repr

def doSomething():
    
    with open("input.txt") as fp:
        allLines = fp.read().splitlines()
    
    
    allValues = {}
    
    currentMask = ""
    
    for line in allLines:
        
        
        if "mask" in line:
            currentMask = line.split(' ')[2]
            # print("New mask: " + currentMask)
            continue
        
        print("\n")
        
        line_sp = line.split(' ')
        index_1 = line_sp[0].split('[')
        index = int(index_1[1][:-1])
        value = int(line_sp[2])
        
        index_bin = binary_repr(index, 36)
        
        result = ""
        
        for i in range(36):
            if currentMask[i] == 'X':
                result += "X"
            else:
                result += str(int(currentMask[i]) or int(index_bin[i]))
        
        print("address: " + str(index_bin) + "  (decimal " + str(int(index_bin, 2)) + ")")
        print("mask:    " + str(currentMask))
        print("result:  " + result)
        print()
        
        currentAddressList = getAddresses(result)
        
        for add in currentAddressList:
            allValues[add] = value
    
    print("\n\n################################")
    print("Summe: " + str(sum(allValues.values())))
        


def getAddresses(mask):
    print("Getting addresses")
    allValues = []
    
    x_count = mask.count('X')
    iterVal = 2 ** x_count
    
    # iterRange = list(range(iterVal))
    # print(iterRange)
    
    for i in range(iterVal):
        i_bin = binary_repr(i, x_count)
        repl_index = 0
        app_st = ""
        for j in range(len(mask)):
            if mask[j] == 'X':
                app_st += i_bin[repl_index]
                repl_index += 1
            else:
                app_st += mask[j]
        
        allValues.append(str(int(app_st, 2)))
    
    # print(allValues)
    
    return allValues


def ex_a():
    currentMask = ""
    for line in allLines:
        print("\n--------------------------------\n")
        print("Line: " + line)
        
        if "mask" in line:
            currentMask = line.split(' ')[2]
            print("New mask: " + currentMask)
            continue
        
        line_sp = line.split(' ')
        index_1 = line_sp[0].split('[')
        index = int(index_1[1][:-1])
        value = int(line_sp[2])
        value_bin = binary_repr(value, 36)
        
        print("Index: " + str(index))
        print("Number: " + str(value))
        print("Number bin: " + value_bin)
        
        bin_st = ""
        for i in range(36):
            mask_val = currentMask[i]
            if mask_val != 'X':
                bin_st += mask_val
            else:
                bin_st += value_bin[i]
        
        print()
        print("value:  " + value_bin + "  (decimal " + str(int(value_bin, 2)) + ")")
        print("mask:   " + currentMask)
        print("result: " + bin_st + "  (decimal " + str(int(bin_st, 2)) + ")")
        
        allValues[index] = int(bin_st, 2)
    
    print("\n\n################################")
    print("Summe: " + str(sum(allValues.values())))



if __name__== "__main__":
    doSomething()