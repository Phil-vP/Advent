# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:56:46 2020

@author: Philipp
"""

from Bag import Bag

def doSomething():
#if __name__== "__main__":
    
    with open("input.txt") as fp:
        allLines = fp.read().splitlines()
    
    allBagKeys = []
    allBags = {}
    stativ = "lightred"
    
    for l in allLines:
        print(l)
        l_sp = l.split(' ')
        source_color = l_sp[0] + l_sp[1]
        print(source_color)
        
        allBagKeys.append(source_color)
        
        bag_count = l.count("bag") - 1
        if "no other" in l:
            bag_count = 0
#        print(bag_count)
        
        children = {}
        
        for i in range(bag_count):
            child_name = l_sp[5+i*4] + l_sp[6+i*4]
            children[child_name] = int(l_sp[4+i*4])
#            children.append(l_sp[5+i*4] + l_sp[6+i*4] + ": " + l_sp[4+i*4])
        
#        print(children)
        
        b = Bag(source_color)
        b.setNachfolgerMap(children)
        allBags[source_color] = b
    
    for b in allBagKeys:
        allBags[b].calcNachfolgerToBag(allBags)
    
    print(allBags["shinygold"].getNumber() - 1)
    
    
    
    
def first():
    
    count = 0
    
    for k in list(allBags.keys()):
        current_bag = allBags[k]
        print(current_bag.name)
        nachfolger = []
        nachfolger.extend(current_bag.getNachfolger())
        
        visited_nachfolger = []
        
        while len(nachfolger) != 0:
            current = nachfolger.pop(0)
            
            if current in visited_nachfolger:
                continue
            visited_nachfolger.append(current)
            
            nachfolger.extend(allBags[current].getNachfolger())
        
        if "shinygold" in visited_nachfolger:
            count += 1
    
    
    print("Count: " + str(count))
        
        
#    print(allBagKeys)
    
    
    
    
    
    # fout = open("output.txt", "w+")
    # fout.write("Moinsen")
    # fout.close()

if __name__== "__main__":
    doSomething()