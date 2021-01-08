# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:56:46 2020

@author: Philipp
"""

import numpy
import itertools

def doSomething():
    
    with open("input.txt") as fp:
        allLines = fp.read().splitlines()
    
    allTickets = []
    ownTicket = ""
    
    allConstraints = {}
    
    constraintCheck = True
    ownTicketCheck = True
    
    for l in allLines:
        if constraintCheck:
            if l == "":
                constraintCheck = False
            else:
                sp = l.split(': ')
                print(sp[1])
                allConstraints[sp[0]] = sp[1]
        
        elif ownTicketCheck:
            if l == "":
                ownTicketCheck = False
            else:
                if "," in l:
                    ownTicket = l.split(",")
        
        else:
            # all Tickets
            if "," in l:
                allTickets.append(l)
    
    bigRange = []
    
    fieldConstrains = {}
    
    for k in list(allConstraints.keys()):
        value = allConstraints[k]
        spl = value.split(" or ")
        thisRange = []
        for sp in spl:
            split = sp.split("-")
            limit1 = int(split[0])
            limit2 = int(split[1])
            for r in range(limit1, limit2+1):
                if r not in bigRange:
                    bigRange.append(r)
            thisRange.extend(list(range(limit1, limit2)))
        fieldConstrains[k] = thisRange
        
    
    bigRange.sort()
    # print(bigRange)
    
    print("Number of all Tickets: " + str(len(allTickets)))
    
    removeTickets = []
    
    for t in allTickets:
        removal = False
        spl = t.split(",")
        for s in spl:
            x = int(s)
            # print("Is " + s + " in the Range? " + str(x in bigRange))
            if x not in bigRange:
                removal = True
                # print(s + " not in range")
                # break
        
        if removal:
            # print("Removing the ticket " + t)
            removeTickets.append(t)
        # print()
    
    for r in removeTickets:
        allTickets.remove(r)
    
    
    print("Number of valid Tickets: " + str(len(allTickets)))
    # print("\nAll valid tickets:")
    # for t in allTickets:
        # print(t)
    
    for tPos in range(len(allTickets)):
        allTickets[tPos] = allTickets[tPos].split(",")
    
    print("All constraints:")
    for k in list(allConstraints.keys()):
        print(k + ": " + allConstraints[k])
    
    print("\nOwn Ticket: " + str(ownTicket))
    number_entries = len(ownTicket)
    print("Number of entries per ticket: " + str(number_entries))
    
    # print("\nAll other tickets:")
    
    # for t in allTickets:
        # print(t)
    
    allTicketsArray = numpy.array(allTickets)
    print(allTicketsArray)
    
    print("Number of all Tickets: " + str(len(allTickets)))
    
    constraintRanges = {}
    
    for c in list(allConstraints.keys()):
        allRangeStr = allConstraints[c]
        allRange_split = allRangeStr.split(" or ")
        # print(allRangeStr)
        print(str(c) + ": " + str(allRange_split))
        this_range = []
        for sp in allRange_split:
            spl = sp.split("-")
            ran = range(int(spl[0]), int(spl[1])+1)
            this_range.extend(ran)
        this_range.sort()
        # print(this_range)
        # print()
        constraintRanges[c] = this_range
    
    allTicketValues = {}
    
    for position in range(number_entries):
        allTicketValues[position] = allTicketsArray[:,position]
        # print("Position " + str(position) + ": " + str(allTicketValues[position]))
    
    
    combination_array = numpy.ones((number_entries, number_entries), numpy.int8)
    print(combination_array)
    
    constraintKeysSorted = list(allConstraints.keys())
    constraintKeysSorted.sort()
    
    for position in range(number_entries):
        column = -1
        allValPos = allTicketValues[position]
        
        for key in constraintKeysSorted:
            column += 1
            set_value = 1
            range_check = constraintRanges[key]
            for value in allValPos:
                if int(value) not in range_check:
                    set_value = 0
                    # print("Error: " + str(value) + " not in " + str(key))
            
            combination_array[position][column] = set_value
        
        # print(combination_array)
        # print("-----")
    
    # Initial checks completed, now the fun begins:
    
    for position in range(number_entries):
        print("Position: " + str(position))
        comp = itertools.compress(constraintKeysSorted, combination_array[position])
        print(str(list(comp)))
        print()
    
    doneSomething = True
    alreadyDone = [False] * number_entries
    
    while doneSomething:
        doneSomething = False
        for position in range(number_entries):
            if not alreadyDone[position] and sum(combination_array[position]) == 1:
                
                print("Found something at position " + str(position))
                alreadyDone[position] = True
                doneSomething = True
                
                for i in range(number_entries):
                    if not sum(combination_array[i]) == 1:
                        # print("Calculating " + str(combination_array[i]) + " - " + str(combination_array[position]))
                        combination_array[i] -= combination_array[position]
        print(combination_array)
    
    
    final_list = {}
    
    for position in range(number_entries):
        print("Position: " + str(position))
        comp = list(itertools.compress(constraintKeysSorted, combination_array[position]))
        final_list[position] = str(comp[0])
        print(str(comp))
        print()
    
    
    
    mult = 1
    for position in range(number_entries):
        if "departure" in final_list[position]:
            mult *= int(ownTicket[position])
    
    print(ownTicket)
    print(mult)
    
    
    

if __name__== "__main__":
    doSomething()