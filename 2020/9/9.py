# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:56:46 2020

@author: Philipp
"""

import itertools

def doSomething():
    
    with open("input.txt") as fp:
        allLines = fp.read().splitlines()
    
    numbers = []
    for l in allLines:
        numbers.append(int(l))

    ex_b(numbers)


def ex_b(numbers):
    
    # target = 127
    target = 70639851
    
    for i in range(len(numbers)):
        for it in range(i, 0, -1):
            rng = numbers[it:i]
            summe = sum(rng)
            print(summe)
            if summe > target:
                print("Bigger, breaking to avoid " + str(i-it)  + " loops")
                break
            if summe == target:
                print("Found!: " + str(rng))
                print("Small: " + str(min(rng)))
                print("Big: " + str(max(rng)))
                print("Summe: " + str(min(rng) + max(rng)))
                return


def ex_a():
    allLines = []
    numbers = []
    
    print(allLines)
    print(numbers)
    
    combination = 25
    
    
    for i in range(combination, len(numbers)):
        found = False
        print(numbers[i-combination:i])
        print(numbers[i])
        
        prevList = numbers[i-combination:i]
        number = numbers[i]
        
        for tupel in itertools.combinations(prevList, 2):
            # print(tupel)
            if sum(tupel) == number:
                found = True
                break
        
        if not found:
            print("Number found: " + str(number))
            break
        
        print()
    
    # fout = open("output.txt", "w+")
    # fout.write("Moinsen")
    # fout.close()

if __name__== "__main__":
    doSomething()