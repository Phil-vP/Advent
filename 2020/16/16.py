# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:56:46 2020

@author: Philipp
"""

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
                sp = l.split(':')
                allConstraints[sp[0]] = sp[1]
        
        elif ownTicketCheck:
            if l == "":
                ownTicketCheck = False
            else:
                if "," in l:
                    ownTicket = l
        
        else:
            # all Tickets
            if "," in l:
                allTickets.append(l)
    
    print("All constraints:")
    for k in list(allConstraints.keys()):
        print(k + ": " + allConstraints[k])
    
    print("\nOwn Ticket: " + ownTicket)
    
    print("\nAll other tickets:")
    for t in allTickets:
        print(t)
    
    
    bigRange = []
    
    for c in list(allConstraints.values()):
        spl = c.split(" or ")
        for sp in spl:
            split = sp.split("-")
            limit1 = int(split[0])
            limit2 = int(split[1])
            for r in range(limit1, limit2+1):
                if r not in bigRange:
                    bigRange.append(r)
    
    bigRange.sort()
    # print(bigRange)
    
    print("Number of all Tickets: " + str(len(allTickets)))
    
    removeTickets = []
    
    for t in allTickets:
        removal = False
        spl = t.split(",")
        for s in spl:
            x = int(s)
            print("Is " + s + " in the Range? " + str(x in bigRange))
            if x not in bigRange:
                removal = True
                print(s + " not in range")
                # break
        
        if removal:
            print("Removing the ticket " + t)
            removeTickets.append(t)
        print()
    
    for r in removeTickets:
        allTickets.remove(r)
    
    
    print("Number of valid Tickets: " + str(len(allTickets)))
    print("\nAll valid tickets:")
    for t in allTickets:
        print(t)
    
    

def ex_a():
    bigRange = []
    
    for c in list(allConstraints.values()):
        spl = c.split(" or ")
        for sp in spl:
            split = sp.split("-")
            limit1 = int(split[0])
            limit2 = int(split[1])
            for r in range(limit1, limit2+1):
                if r not in bigRange:
                    bigRange.append(r)
    
    bigRange.sort()
    print(bigRange)
    
    notVals = []
    
    for t in allTickets:
        spl = t.split(",")
        for s in spl:
            x = int(s)
            if x not in bigRange:
                notVals.append(x)
    
    print("Final value: " + str(sum(notVals)))
    
    # fout = open("output.txt", "w+")
    # fout.write("Moinsen")
    # fout.close()

if __name__== "__main__":
    doSomething()