# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:56:46 2020

@author: Philipp
"""

import itertools


def doSomething():
    
    multi = [1, 1, 2, 4, 7, 13, 24, 44, 81, 1, 1]
    
    with open("input.txt") as fp:
        allLines = fp.read().splitlines()
    
    adapters = []
    
    for l in allLines:
        adapters.append(int(l))
    
    
    own_device = max(adapters) + 3
    adapters.append(own_device)
    adapters.sort()
    
    current_jolt = 0
    search_str = ""
    
    for ad in adapters:
        diff = ad - current_jolt
        search_str += str(diff)
        print("Current: " + str(current_jolt) + " --> " + str(ad) + ": " + str(diff))
        current_jolt = ad
    
#    search_str = "13111131113133"
    
    print(search_str)
    
    occ = [0] * 11
    
    for i in range(10, 1, -1):
        st = "1" * i
        st_count = search_str.count(st)
        
        for j in range(2, i):
            occ[j] -= st_count
        occ[i] += st_count
        
#        print("i: " + str(i) + ", Occurrences in String: " + str(search_str.count(st)))
    
    for i in range(len(occ)):
        print("i: " + str(i) + ", Occurrences in String: " + str(occ[i]))

    ergebnis = 1
    for i in range(2, len(occ)):
        for j in range(occ[i]):
            print("Multiplied by " + str(multi[i]))
            ergebnis *= multi[i]
    
    print(ergebnis)
    
    

def ex_A():
    
    adapters = []
    own_device = max(adapters) + 3
    adapters.append(own_device)
    adapters.sort()
    
    print("Own device rating: " + str(own_device))
    
    current_jolt = 0
    numbers = [0] * 5
    
    for ad in adapters:
        diff = ad - current_jolt
        numbers[diff] += 1
        print("Current: " + str(current_jolt) + " --> " + str(ad) + ": " + str(diff))
        current_jolt = ad

    


    ergebnis = numbers[1] * numbers[3]
    print("difference 1: " + str(numbers[1]))
    print("difference 3: " + str(numbers[3]))
    print("Ergebnis: " + str(ergebnis))
        
    
    # fout = open("output.txt", "w+")
    # fout.write("Moinsen")
    # fout.close()


def getPerms():
    
    
    fout = open("output.txt", "w+")
#    fout.write("Moinsen")
    
    
    allcombs = [[]] * 15
    
    for i in range(3,10):
        r = list(range(i))
        print(r)
        comb = []
        for j in range(2, i+1):
            comb += list(itertools.combinations(r, j))
        
        allcombs[i] = comb
    
    for i in range(3, 10):
        print("i: " + str(i))
        counter = 0
        for c in allcombs[i]:
            if isvalid(c, i, fout):
                counter += 1
                if i < 5:
                    print(c)
        print("Counter for i = " + str(i) + ": " + str(counter))
        print("#######################")
        fout.write("Counter for i = " + str(i) + ": " + str(counter) + "\n")
        fout.write("\n#######################\n\n")
    
    fout.close()

def isvalid(c, i, fout):
    if c[0] != 0:
        fout.write(str(c) + " is not valid, because c[0] != 0\n")
        return False
    if c[-1] != i-1:
        fout.write(str(c) + " is not valid, because c[-1] != " + str(i-1) + "\n")
        return False
    
    for j in range(len(c) -1):
        if c[j+1] - c[j] > 3:
            fout.write(str(c) + " is not valid, as " + str(c[j+1]) + " - " + str(c[j]) + " > 3\n")
            return False
    
    fout.write(str(c) + " is valid\n")
    return True


if __name__== "__main__":
    doSomething()
#    getPerms()