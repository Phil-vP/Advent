# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 10:56:01 2020

@author: Philipp
"""
numberOfCards = 10007
#numberOfCards = 10

def doSomething():
    global numberOfCards
    allCards = []
    for x in range(numberOfCards):
        allCards.append(x)
    #print(allCards)
    #allCards = dealIntoNewStack(allCards)
    #allCards = cardCut(allCards, -4)
    #allCards = dealWithIncrement(allCards, 3)
    #print(allCards)
    with open("input.txt") as f:
        lines = f.readlines()
    for l in range(len(lines)):
        lines[l] = lines[l].strip()
        
    print("starting")
    
    for l in lines:
        if "into" in l:
            allCards = dealIntoNewStack(allCards)
        elif "with" in l:
            newList = l.split(" ")
            allCards = dealWithIncrement(allCards, int(newList[-1]))
        elif "cut" in l:
            newList = l.split(" ")
            allCards = cardCut(allCards, int(newList[-1]))
        else:
            print("ERROR, line: " + l)
    
    print(allCards)
    print("Index: " + str(allCards.index(2019)))
        

def dealIntoNewStack(deck):
    deck.reverse()
    return deck

def cardCut(deck, number):
    list1 = deck[:number]
    list2 = deck[number:]
    print("list1: " + str(list1))
    print("list2: " + str(list2))
    list2.extend(list1)
    return list2

def dealWithIncrement(deck, inc):
    global numberOfCards
    newDeck = [0]*numberOfCards
    for x in range(numberOfCards):
        newDeck[(x*inc)%numberOfCards] = deck[x]
    return newDeck

if __name__== "__main__":
    doSomething()