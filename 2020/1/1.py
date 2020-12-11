# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:56:46 2020

@author: Philipp
"""

import itertools
import math

def doSomething():
    
    with open("input.txt") as fp:
        allLines = fp.read().splitlines()
    
    # print(allLines)
    
    number_arr = []
    for line in allLines:
        number_arr.append(int(line))
    
    print(number_arr)
    
    iter_list = itertools.combinations(number_arr, 3)
    
    for i in iter_list:
        if sum(i) == 2020:
            print(i)
            print(math.prod(i))
    

def one_a(allLines):
    bool_array = [False] * 2021
    
    for line in allLines:
        number = int(line)
        t_minus = 2020 - number
        
        # print("\nNumber: " + str(number) + ", t_minus: " + str(t_minus))
        
        if not bool_array[t_minus]:
            bool_array[number] = True
            # print(str(number) + " is not true yet, it is now set")
            continue
        else:
            print("Numbers found: " + str(number) + " * " + str(t_minus) + " = " + str(number * t_minus))
            return
    
    print("Sad story")
    
        
    # fout = open("output.txt", "w+")
    # fout.write("Moinsen")
    # fout.close()

if __name__== "__main__":
    doSomething()