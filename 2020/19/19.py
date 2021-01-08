# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:56:46 2020

@author: Philipp
"""

import itertools

allRules = {}

def doSomething():
    global allRules
    
    with open("input.txt") as fp:
        allLines = fp.read().splitlines()
    
    found_split = False
    
    allStrings = []
    
    for l in allLines:
        if l == "":
            found_split = True
            continue
        
        if not found_split:
            sp = l.split(": ")
            allRules[int(sp[0])] = sp[1]
        else:
            allStrings.append(l)
    
    allKeysSorted = list(allRules.keys())
    allKeysSorted.sort()
    
    for key in allKeysSorted:
        print(str(key) + ": " + allRules[key])
    
    final_list = franz(0)
    
    # for le in final_list:
        # print(le)
    
    print(str(len(final_list)) + " Rules to follow")
    
    
    print(str(len(allStrings)) + " Strings to check:")
    # print(allStrings)
    
    counter = 0
    
    for string in allStrings:
        if string in final_list:
            counter += 1
    
    print("Final counter: " + str(counter))
    


def franz(currentRule):
    # print("IN RULE " + str(currentRule))
    myRule = allRules[currentRule]
    ret_list = []
    
    if myRule.islower():
        rep = myRule.replace("\"", "")
        ret_list.append(rep)
        # print("returning simple letter\n")
        return ret_list
    
    rules_this_iter = []
    
    if "|" in myRule:
        rules_this_iter = myRule.split(" | ")
    else:
        rules_this_iter.append(myRule)
    
    # print("currentRule: " + str(currentRule))
    # print("myRule: " + myRule)
    # print(rules_this_iter)
    
    for rule in rules_this_iter:
        # print("currentRule: " + str(currentRule) + ", rule: " + str(rule) + ", type: " + str(type(rule)))
        sp = rule.split(" ")
        currentList = franz(int(sp[0]))
        for i in range(1, len(sp)):
            newList = list(itertools.product(currentList, franz(int(sp[i]))))
            currentList = [''.join(i) for i in newList]
            
        ret_list.extend(currentList)
    
    return ret_list
        

if __name__== "__main__":
    doSomething()
    # print("moin")
    # print("moin".replace("o", ""))