# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:56:46 2020

@author: Philipp
"""

def doSomething():
    
    with open("input.txt") as fp:
        allLines = fp.read().splitlines()
    
    size = 26
    
    all_groups = []
    currentGroup = [0] * size
    
    lineCount = 0
    
    for line in allLines:
        if line == '':
            currentGroup.append(lineCount)
            all_groups.append(currentGroup)
#            print(currentGroup)
            currentGroup = [0] * size
            lineCount = 0
            continue
        lineCount += 1
        
        for c in line:
            currentGroup[ord(c)-97] += 1
    
    currentGroup.append(lineCount)
    all_groups.append(currentGroup)
    
    count = -1 * len(all_groups)
    
#    total_count = 0
        
    for g in all_groups:
        print(g)
#        count = -1
        last = g[-1]
        
        for q in g:
            if q == last:
                count += 1
#        print("GroupCount: " + str(count))
#        total_count += count
    
#    print(total_count)
    print(count)
        

def end_a():
    summe = 0
    
    for g in all_groups:
        summe += sum(g)
        print(g)
    
    print()
    print(summe)
    
    # fout = open("output.txt", "w+")
    # fout.write("Moinsen")
    # fout.close()

if __name__== "__main__":
    doSomething()